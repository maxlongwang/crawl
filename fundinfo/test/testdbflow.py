import cx_Oracle
import pymysql

# 连接Oracle数据库
oracle_connection = cx_Oracle.connect('rdmetl', 'oracle', '192.168.146.164/uf')
oracle_cursor = oracle_connection.cursor()

# 连接MySQL数据库
mysql_connection = pymysql.connect(host='192.168.144.141', user='rdmetl', password='mysql',database='casset')
mysql_cursor = mysql_connection.cursor()

# 从Oracle获取数据
oracle_cursor.execute("SELECT * FROM casset.ads_tag_asset_model")
rows = oracle_cursor.fetchall()

# 将数据插入到MySQL
for row in rows:
    # 假设MySQL表结构与Oracle表结构相同
    mysql_cursor.execute("INSERT INTO ads_tag_asset_model VALUES (%s, %s)", row)

# 提交MySQL事务
mysql_connection.commit()

# 关闭MySQL和Oracle连接
mysql_cursor.close()
mysql_connection.close()
oracle_cursor.close()
oracle_connection.close()