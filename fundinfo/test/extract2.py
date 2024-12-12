import cx_Oracle
import pymysql
from concurrent.futures import ThreadPoolExecutor,as_completed
from  extract import now


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

def extract_data_from_oracle():
    # 连接Oracle数据库
    oracle_conn = cx_Oracle.connect(**oracle_config)
    oracle_cursor = oracle_conn.cursor()

    # 查询数据
    oracle_cursor.execute("SELECT * FROM casset.ads_tag_asset_model ")
    rows = oracle_cursor.fetchall()

    # 获取列名
    column_names = [desc[0] for desc in oracle_cursor.description]

    # 关闭Oracle连接
    oracle_cursor.close()
    oracle_conn.close()

    return column_names, rows

def load_data_to_mysql(column_names, rows):
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
    print('extract from oracle beign',now())
    column_names, rows = extract_data_from_oracle()
    print('extract from oracle end',now())
        # 定义每个线程处理的数据量
    batch_size = 100000
    futures = []

    print('multi thread submit beign',now())
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(0, len(rows), batch_size):
            batch_rows = rows[i:i + batch_size]
            futures.append(executor.submit(load_data_to_mysql, column_names,batch_rows))
        print('multi thread submit end',now())
        # 等待所有线程完成
        print('futures begin',now())
        for future in as_completed(futures):
            try:
                future.result()  # 获取结果，若有异常会抛出
                print(f"Batch imported successfully.{now()}")
            except Exception as e:
                print(f"Error occurred: {e}")
        print('futures end',now())
                
    # load_data_to_mysql(column_names, rows)
    # print("数据成功从Oracle迁移到MySQL！")

if __name__ == "__main__":
    main()
