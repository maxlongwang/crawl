import cx_Oracle
import pymysql
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime


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
placeholders = None
insert_query = None

oracle_conn = cx_Oracle.connect(**oracle_config)
oracle_cursor = oracle_conn.cursor()
mysql_conn = pymysql.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor()


def extract_data_from_oracle(batch_size):
    # 连接Oracle数据库
    global column_names,placeholders,insert_query
    # 查询数据
    oracle_cursor.execute("SELECT * FROM casset.ads_tag_asset_model ")
    column_names = [desc[0] for desc in oracle_cursor.description]
    placeholders = ', '.join(['%s'] * len(column_names))
    insert_query = f"INSERT INTO ads_tag_asset_model2 ({', '.join(column_names)}) VALUES ({placeholders})"
    while True:
        # 按批次提取数据
        rows = oracle_cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows


def load_data_to_mysql(insert_query, rows):
    # 插入数据
    mysql_cursor.executemany(insert_query, rows)

    # 提交事务
    mysql_conn.commit()


def main():
    batch_size = 2000

    # 提取数据并导入
    for rows in extract_data_from_oracle(batch_size):
        # if column_names is None:
        #     # 获取列名
        #     column_names = [desc[0] for desc in rows[0].cursor.description]
        # 构建插入语句

        load_data_to_mysql(insert_query, rows)
        # print(f"Imported {len(rows)} records to MySQL.{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

        # 关闭Oracle连接
    oracle_cursor.close()
    oracle_conn.close()
    # 关闭MySQL连接
    mysql_cursor.close()
    mysql_conn.close()


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    main()
