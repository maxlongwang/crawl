
import datetime
import cx_Oracle
print(cx_Oracle.version)
# 1616189675
# timestamp = 1379808  # 示例时间戳
# converted_time = datetime.datetime.fromtimestamp(timestamp)
# print(type(converted_time))
# time=str(converted_time)
# print(type(time))
# print(time)

# timestamp = 1632919327
# date_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
# print(date_time)


# i=1
# base_url="https://gs.amac.org.cn/amac-infodisc/api/pof/fund?&page={}&size=20"
# while(i<=10):
#     next_page_url=base_url.format(i)
#     print(next_page_url)
#     i=i+1
