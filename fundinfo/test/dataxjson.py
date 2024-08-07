import cx_Oracle
import json
import pandas as pd

create_column_names = ''
s_columns_list = []
t_columns_list = []
filename=''


def getColumns(s_username, s_password, dburl):
    global create_column_names, s_columns_list, t_columns_list
    conn = cx_Oracle.connect(s_username, s_password, dburl)
    cursor = conn.cursor()
    sql = f'''
    select column_name,
       data_type2 || case
         when data_type2 = 'DECIMAL' and data_precision is not null then
          '(' || data_precision || ',' || data_scale || ')'
         when data_type2 = 'DECIMAL' and data_precision is null then
          '(' || data_length || ',4)'
         when data_type2 in ('CHAR', 'VARCHAR') then
          '(' || data_length || ')'
       end data_type3
  from (select column_name,
               data_type,
               data_precision,
               data_scale,
               case
                 when data_type = 'VARCHAR2' then
                  'VARCHAR'
                 when data_type = 'NUMBER' then
                  case
                    when data_precision is null and column_name in ('INIT_DATE') then
                     'INT'
                    when data_scale = 0 and data_precision = 19 then
                     'BIGINT'
                    when data_scale = 0 and data_precision = 10 then
                     'INT'
                    else
                     'DECIMAL'
                  end
                 when data_type = 'CLOB' then
                  'TEXT'
                 else
                  data_type
               end data_type2,
               data_length
          from user_tab_columns t
         where table_name = '{s_tablename.upper()}'
         order by column_id)
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    s_columns_list = []
    create_column_name_list = []
    t_columns_list = []
    for row in result:
        column_name = row[0]
        s_column = '{}'.format(column_name)
        s_columns_list.append(s_column)

        t_column = '`{}`'.format(column_name.lower())
        t_columns_list.append(t_column)

        create_column_name = f'{row[0]} {row[1]}'
        create_column_name_list.append(create_column_name.lower())

    cursor.close()
    conn.close()

    create_column_names = ','.join(create_column_name_list)


def generate_json_file(s_jdbcurl, s_tablename, s_username, s_password, t_jdbcurl, t_tablename, t_username, t_password, s_columns_list, t_columns_list,sync_type,sync_colname):
    # tablename_dbname_username_o2m.json
    global filename
    with open("./template/oracle2mysql.json", "r") as file:
        json_data = json.load(file)

    json_data['job']['content'][0]['reader']['parameter']['connection'][0]['jdbcUrl'][0] = s_jdbcurl
    json_data['job']['content'][0]['reader']['parameter']['connection'][0]['table'][0] = s_tablename
    json_data['job']['content'][0]['reader']['parameter']['column'] = s_columns_list
    json_data['job']['content'][0]['reader']['parameter']['password'] = s_password
    json_data['job']['content'][0]['reader']['parameter']['username'] = s_username
    json_data['job']['content'][0]['writer']['parameter']['connection'][0]['jdbcUrl'] = t_jdbcurl
    json_data['job']['content'][0]['writer']['parameter']['connection'][0]['table'][0] = t_tablename
    json_data['job']['content'][0]['writer']['parameter']['column'] = t_columns_list
    json_data['job']['content'][0]['writer']['parameter']['password'] = t_password
    json_data['job']['content'][0]['writer']['parameter']['username'] = t_username
    
    # 全量
    if sync_type==1:
        preSql=[]
        preSql_str=f"delete from {t_tablename}"
        preSql.append(preSql_str)
        json_data['job']['content'][0]['writer']['parameter']['preSql']=preSql
    # 按天
    elif (sync_type==2):
        json_data['job']['content'][0]['reader']['parameter']['where']= f"{sync_colname} between to_date('${{start_date}}','yyyymmdd') and to_date('${{end_date}}','yyyymmdd')"
        preSql_str=f"delete from {t_tablename} where {sync_colname} between '${{start_date}}' and '${{end_date}}'"
        preSql=[]
        preSql.append(preSql_str)
        json_data['job']['content'][0]['writer']['parameter']['preSql']=preSql
    # 按主键增量
    elif (sync_type==3):
        json_data['job']['content'][0]['reader']['parameter']['where']= f"{sync_colname}>'${{{sync_colname}}}'"
        #jydb 需要删除数据
        if (t_jdbcurl.split('/')[-1]=='jydb'):
            postSql_str=f"delete from {t_tablename} where jsid in (select jsid from jydb_deleterec where tablename='{t_tablename}' and xgrq>DATE(NOW()))"
            postSql=[]
            postSql.append(postSql_str)
            json_data['job']['content'][0]['writer']['parameter']['postSql']=postSql
            
        
    with open(f'./output/json/{filename}.json', 'w') as file:
        json.dump(json_data, file, indent=4)


def create_table(table_name, t_columns):
    # tablename = table_name.lower()
    a = f'create table {table_name} ({t_columns})'
    with open(f'./output/sql/{table_name}.sql', 'w') as f:
        f.write(a)


def generate_pre_json_file(table_name, column_name,t_jdbcurl,t_username,t_password):
    global filename
    with open("./template/oracle2mysql_pre.json", "r") as file:
        json_data = json.load(file)
        json_data['job']['content'][0]['reader']['parameter']['connection'][0]['jdbcUrl'][0] = t_jdbcurl
        querySql = f'SELECT ifnull(max({column_name}),0) FROM {table_name}'
        json_data['job']['content'][0]['reader']['parameter']['connection'][0]['querySql'][0] = querySql
        
        json_data['job']['content'][0]['writer']['parameter']['fileName'] = f'{filename}_{column_name}'
        json_data['job']['content'][0]['reader']['parameter']['username'] = t_username
        json_data['job']['content'][0]['reader']['parameter']['password'] = t_password

    with open(f'./output/json_pre/{filename}_pre.json', 'w') as file:
        json.dump(json_data, file, indent=4)


# main()
df = pd.read_excel('table_oracle2mysql.xlsx')

for _, row in df.iterrows():
    s_tablename = row['s_tablename']
    s_jdbcurl = row['s_jdbcurl']
    s_username = row['s_username']
    s_password = row['s_password']
    t_tablename = row['t_tablename']
    t_jdbcurl = row['t_jdbcurl']
    t_username = row['t_username']
    t_password = row['t_password']
    sync_type= row['sync_type']
    sync_colname = row['sync_colname']
    

    dburl = s_jdbcurl.split('@')[-1]
    filename = f'{t_jdbcurl.split('/')[-1]}_{t_tablename}'

    getColumns(s_username, s_password, dburl)
    create_table(t_tablename, create_column_names)
    generate_json_file(s_jdbcurl, s_tablename, s_username, s_password, t_jdbcurl, t_tablename, t_username, t_password, s_columns_list, t_columns_list,sync_type,sync_colname)
    if (sync_type==3):
        generate_pre_json_file(s_tablename, sync_colname,t_jdbcurl,t_username,t_password)
    

