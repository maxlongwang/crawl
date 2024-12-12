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

def extract_data_from_oracle(batch_size):
    # 连接Oracle数据库
    oracle_conn = cx_Oracle.connect(**oracle_config)
    oracle_cursor = oracle_conn.cursor()
    global column_names

    # 查询数据
    oracle_cursor.execute("SELECT * FROM casset.ads_tag_asset_model ")
    column_names=[desc[0] for desc in oracle_cursor.description]
    while True:
        # 按批次提取数据
        rows = oracle_cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows

    # 关闭Oracle连接
    oracle_cursor.close()
    oracle_conn.close()


def load_data_to_mysql(rows, column_names):
    # 连接MySQL数据库
    mysql_conn = pymysql.connect(**mysql_config)
    mysql_cursor = mysql_conn.cursor()

    # 构建插入语句
    placeholders = ', '.join(['%s'] * len(column_names))
    insert_query = f"INSERT INTO ads_tag_asset_model2 ({', '.join(column_names)}) VALUES ({placeholders})"

    # 插入数据
    mysql_cursor.executemany(insert_query, rows)

    # 提交事务
    mysql_conn.commit()

    # 关闭MySQL连接
    mysql_cursor.close()
    mysql_conn.close()


def main():
    batch_size = 10000

    # 提取数据并导入
    for rows in extract_data_from_oracle(batch_size):
        # if column_names is None:
        #     # 获取列名
        #     column_names = [desc[0] for desc in rows[0].cursor.description]

        load_data_to_mysql(rows, column_names)
        print(f"Imported {len(rows)} records to MySQL.{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    main()