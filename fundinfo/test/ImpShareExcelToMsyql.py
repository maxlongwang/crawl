import pymysql
import requests
# conn = pymysql.connect(host="192.168.144.222", user="root", password="IkE==3rB;P5", database="cetl")
# cursor = conn.cursor()
# cursor.execute("select group_id,dbname,tablename,stablename,sjdbc,susername,spassword,sync_type,incr_col from t_job where status=0")
# results = cursor.fetchall()
# cursor.close()
# conn.close()

response=requests.get('https://docs.qq.com/sheet/DUGRnc1lPa1FRbWJl?is_no_hook_redirect=1&tab=kzuoav')
print(response.text)
# data=response.json()
# print(data)