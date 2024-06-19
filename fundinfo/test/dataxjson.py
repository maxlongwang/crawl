import cx_Oracle
import json

dburl = '192.168.146.164/uf'
username = 'system'
password = 'oracle'


jdbcUrl = f'jdbc:oracle:thin:@{dburl}'
s_username = 'ct11'
s_password = 'oracle'

t_username = 'root'
t_password = 'IkE==3rB;P5'
t_jdbcdbUrl = 'jdbc:mysql://192.168.144.222:3306/cactivity'
table_name = 'PRODCODE'
file_table_name = table_name.lower()
t_table_name = file_table_name

conn = cx_Oracle.connect(username, password, dburl)
cursor = conn.cursor()
sql = f'''
select lower(column_name) column_name,
       lower(data_type2 || case
               when data_type = 'NUMBER' and data_precision is not null then
                '(' || data_length || ',4)'
               when data_type in ('CHAR', 'VARCHAR2') then
                '(' || data_length || ')'
             end) data_type3
  from (select column_name,
               data_type,
               data_precision,
               case
                 when data_type = 'VARCHAR2' then
                  'VARCHAR'
                 when data_type = 'NUMBER' and data_precision is not null then
                  'DECIMAL'
                 when data_type = 'NUMBER' and data_precision is null then
                  'INT'
                 when data_type = 'DATE' then
                  'DATETIME'
                 else
                  data_type
               end data_type2,
               data_length
          from dba_tab_columns t
         where table_name = '{table_name}'
         order by column_id)
 '''
cursor.execute(sql)
result = cursor.fetchall()
# print(result)
co_column_name = []
create_column_name_list=[]
for row in result:
    print(row)
    # print(row[0])
    column_name = row[0]
    column_name2 = '"{}"'.format(column_name)
    co_column_name.append(column_name2)
 
    create_column_name=f'{row[0]} {row[1]}'
    create_column_name_list.append(create_column_name)

cursor.close()
conn.close()
co_column_name3 = ','.join(co_column_name)
create_column_name2=','.join(create_column_name_list)
co_column_name4 = co_column_name3.lower()

with open("./template/oracle2mysql.json", "r") as file:
    json_data = json.load(file)

json_data['job']['content'][0]['reader']['parameter']['connection'][0]['jdbcUrl'][0] = jdbcUrl
json_data['job']['content'][0]['reader']['parameter']['connection'][0]['table'][0] = file_table_name
json_data['job']['content'][0]['reader']['parameter']['column'][0] = co_column_name4
json_data['job']['content'][0]['reader']['parameter']['password'] = s_password
json_data['job']['content'][0]['reader']['parameter']['username'] = s_username
json_data['job']['content'][0]['writer']['parameter']['connection'][0]['jdbcUrl'] = t_jdbcdbUrl
json_data['job']['content'][0]['writer']['parameter']['connection'][0]['table'][0] = t_table_name
json_data['job']['content'][0]['writer']['parameter']['column'][0] = co_column_name4
json_data['job']['content'][0]['writer']['parameter']['password'] = t_password
json_data['job']['content'][0]['writer']['parameter']['username'] = t_username

# print(json_data)

with open(f'./output/{file_table_name}_oralce2mysql.json', 'w') as file:
    json.dump(json_data, file, indent=4)


def create_table(table_name):
    a=f'create table {table_name} ({create_column_name2})'
    print(a)
    with open(f'./output/{file_table_name}.sql', 'w') as f:
        f.write(a)
        
create_table(file_table_name)                    