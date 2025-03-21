import asyncio
from collections import deque
import cx_Oracle
import aiomysql
from datetime import datetime
column_names = None
placeholders = None
insert_query = None


async def oracle_producer(queue):
    # Oracle连接配置
    conn = cx_Oracle.connect('system', 'oracle', '192.168.146.164/uf')
    cursor = conn.cursor()
    batch_size = 10000
    global column_names, placeholders, insert_query

    try:
        cursor.execute("select * from casset.ads_tag_asset_model")
        column_names = [desc[0] for desc in cursor.description]
        placeholders = ', '.join(['%s'] * len(column_names))
        insert_query = f"INSERT INTO ads_tag_asset_model2 ({', '.join(column_names)}) VALUES ({placeholders})"
        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            # 将批次数据放入队列
            await queue.put(rows)
    finally:
        cursor.close()
        conn.close()
        await queue.put(None)  # 结束信号


async def mysql_consumer(queue):
    # MySQL连接池配置
    pool = await aiomysql.create_pool(host='192.168.144.141', user='rdmetl', password='mysql', db='casset', charset='utf8mb4', minsize=5, maxsize=10)

    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            while True:
                batch = await queue.get()
                if batch is None:
                    break
                # 批量插入
                await cursor.executemany(insert_query, batch)
                await conn.commit()

    pool.close()
    await pool.wait_closed()


async def main():
    buffer_queue = asyncio.Queue(maxsize=20)  # 控制内存峰值
    producer = oracle_producer(buffer_queue)
    consumer = mysql_consumer(buffer_queue)
    await asyncio.gather(producer, consumer)

if __name__ == "__main__":
    asyncio.run(main())
