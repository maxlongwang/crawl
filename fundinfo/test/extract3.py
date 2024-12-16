import cx_Oracle
import pymysql
from concurrent.futures import ThreadPoolExecutor, as_completed
from extract import now
from dbutils.pooled_db import PooledDB


# Oracle数据库连接配置
oracle_config = {

    'user': 'rdmetl',
    'password': 'oracle',
    'dsn': '192.168.146.164:1521/uf'
}

# MySQL数据库连接配置
mysql_config = {
    'user': 'rdmetl',
    'password': 'mysql',
    'host': '192.168.144.141',
    'database': 'casset'
}

column_names = None

# 创建连接池
pool = PooledDB(
    creator=pymysql,  # 使用 pymysql 作为连接创建器
    maxconnections=10,  # 最大连接数
    mincached=2,  # 初始化时至少创建的空闲连接数
    maxcached=5,  # 最大空闲连接数
    maxshared=3,  # 最大共享连接数
    blocking=True,  # 如果连接数达到最大，是否阻塞等待
    host='192.168.144.141',
    user='rdmetl',
    password='mysql',
    database='casset'
    # charset='utf8mb4'
)


def get_conn():
    return pool.connection()


def extract_data_from_oracle(batch_size):
    # 连接Oracle数据库
    oracle_conn = cx_Oracle.connect(**oracle_config)
    oracle_cursor = oracle_conn.cursor()

    # 查询数据
    oracle_cursor.execute("SELECT * FROM casset.ads_tag_asset_model ")

    # 获取列名
    global column_names
    column_names = [desc[0] for desc in oracle_cursor.description]

    while True:
        # 按批次提取数据
        rows = oracle_cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows

    # 关闭Oracle连接
    oracle_cursor.close()
    oracle_conn.close()


def load_data_to_mysql(column_names, rows):
    # 连接MySQL数据库
    # mysql_conn = pymysql.connect(**mysql_config)
    # mysql_cursor = mysql_conn.cursor()

    mysql_conn = get_conn()
    mysql_cursor = mysql_conn.cursor()

    # 构建插入语句
    placeholders = ', '.join(['%s'] * len(column_names))
    insert_query = f"INSERT INTO ads_tag_asset_model2 ({', '.join(column_names)}) VALUES ({placeholders})"

    # 插入数据
    mysql_cursor.executemany(insert_query, rows)

    # 提交事务
    mysql_conn.commit()

    # 关闭MySQL连接
    # mysql_cursor.close()
    mysql_conn.close()


def main():
    batch_rows = 30000
    batch_size = 10000

    for rows in extract_data_from_oracle(batch_rows):
        futures = []
        with ThreadPoolExecutor(max_workers=3) as executor:
            for i in range(0, len(rows), batch_size):
                fetch_rows = rows[i:i + batch_size]
                futures.append(executor.submit(load_data_to_mysql, column_names, fetch_rows))

            # 等待所有线程完成
            for future in as_completed(futures):
                try:
                    future.result()  # 获取结果，若有异常会抛出
                    print(f"Batch imported successfully.{now()}")
                except Exception as e:
                    print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
