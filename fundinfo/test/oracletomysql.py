import asyncio
from concurrent.futures import ThreadPoolExecutor
import cx_Oracle
import aiomysql
from typing import List, Tuple

# 配置信息
ORACLE_CONFIG = {
    "user": "casset",
    "password": "oracle",
    "dsn": "192.168.146.164:1521/uf"
}

MYSQL_CONFIG = {
    "host": "192.168.144.141",
    "port": 3306,
    "user": "rdmetl",
    "password": "mysql",
    "db": "casset"
}

# 全局参数
CONCURRENCY = 8    # 并发写入协程数
QUEUE_SIZE = 200000    # 队列缓冲大小
BATCHSIZE = 2000


async def oracle_reader(queue: asyncio.Queue, table: str):
    """Oracle数据读取器(生产者)"""
    loop = asyncio.get_running_loop()
    # 使用线程池执行同步IO操作
    with ThreadPoolExecutor() as pool:
        conn = await loop.run_in_executor(pool, lambda: cx_Oracle.connect(user=ORACLE_CONFIG["user"], password=ORACLE_CONFIG["password"], dsn=ORACLE_CONFIG["dsn"]))
        try:
            cursor = conn.cursor()
            sql = f"select * from {table}"
            cursor.execute(sql)
            while True:
                rows = await loop.run_in_executor(pool, lambda: cursor.fetchmany(BATCHSIZE))
                if not rows:
                    break
                await queue.put((rows, cursor.description))  # 放入数据及元数据
        finally:
            await loop.run_in_executor(pool, conn.close)
    # 发送结束信号
    for _ in range(CONCURRENCY):
        await queue.put((None, None))


async def mysql_writer(queue: asyncio.Queue, table: str):
    """MySQL数据写入器（消费者）"""
    # 创建MySQL连接池
    pool = await aiomysql.create_pool(
        host=MYSQL_CONFIG["host"],
        port=MYSQL_CONFIG["port"],
        user=MYSQL_CONFIG["user"],
        password=MYSQL_CONFIG["password"],
        db=MYSQL_CONFIG["db"],
        minsize=2,
        maxsize=CONCURRENCY
    )
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            while True:
                rows, description = await queue.get()
                try:
                    if rows is None:  # 结束信号
                        break
                    # 构造插入SQL（首次运行时生成）
                    if not hasattr(mysql_writer, 'insert_sql'):
                        col_names = [desc[0] for desc in description]
                        placeholders = ','.join(['%s'] * len(col_names))
                        mysql_writer.insert_sql = (
                            f"INSERT INTO {table}({','.join(col_names)}) "
                            f"VALUES ({placeholders})"
                        )

                    # 批量插入
                    await cursor.executemany(mysql_writer.insert_sql, rows)
                    await conn.commit()

                except Exception as e:
                    print(f"Insert error: {str(e)}")
                    await conn.rollback()
                finally:
                    queue.task_done()


async def main(table_name: str):
    queue = asyncio.Queue(maxsize=QUEUE_SIZE)

    # 启动生产者和消费者
    producers = [asyncio.create_task(oracle_reader(queue, table_name))]
    consumers = [asyncio.create_task(mysql_writer(queue, table_name)) for _ in range(CONCURRENCY)]

    await asyncio.gather(*producers)
    await asyncio.gather(*consumers)

    await queue.join()

    # 取消消费者任务
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    table = "ads_tag_asset_model3"  # 替换为实际表名
    asyncio.run(main(table))
