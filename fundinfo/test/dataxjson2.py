import cx_Oracle
import json
import pymysql

create_column_names = ''
s_columns_list = []
t_columns_list = []
filename = ''


def getColumns(s_username, etl_user,etl_password, dburl,s_tablename):
    global create_column_names, s_columns_list, t_columns_list
    conn = cx_Oracle.connect(etl_user, etl_password, dburl)
    # conn = cx_Oracle.connect('rdmetl', 'oracle', dburl)
    cursor = conn.cursor()
    sql = f'''
    select column_name,
       data_type2 || case
         when data_type2 = 'DECIMAL' and data_precision is not null then
          '(' || data_precision || ',' || data_scale || ')'
         when data_type2 = 'DECIMAL' and data_precision is null then
          '(14,2)'
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
                when data_type='DATE' and column_name='XGRQ' then 
                    'DATETIME'
                 else
                  data_type
               end data_type2,
               data_length
          from dba_tab_columns t
         where table_name = '{s_tablename.upper()}' and owner='{s_username.upper()}'
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


def generate_json_file(s_jdbcurl, s_tablename, s_username, s_password, t_jdbcurl, t_tablename, t_username, t_password, s_columns_list, t_columns_list, sync_type, sync_colname,incr_col_type,etl_user,etl_password,name):
    global filename
    with open("./template/oracle2mysql.json", "r") as file:
        json_data = json.load(file)

    json_data['job']['content'][0]['reader']['parameter']['connection'][0]['jdbcUrl'][0] = s_jdbcurl
    json_data['job']['content'][0]['reader']['parameter']['connection'][0]['table'][0] = f'{s_username}.{s_tablename}'
    json_data['job']['content'][0]['reader']['parameter']['column'] = s_columns_list
    json_data['job']['content'][0]['reader']['parameter']['password'] = etl_password
    json_data['job']['content'][0]['reader']['parameter']['username'] = etl_user
    json_data['job']['content'][0]['writer']['parameter']['connection'][0]['jdbcUrl'] = t_jdbcurl
    json_data['job']['content'][0]['writer']['parameter']['connection'][0]['table'][0] = t_tablename
    json_data['job']['content'][0]['writer']['parameter']['column'] = t_columns_list
    json_data['job']['content'][0]['writer']['parameter']['password'] = t_password
    json_data['job']['content'][0]['writer']['parameter']['username'] = t_username
    
    # jydb 单独处理，按xgrq进行增量的数据抽取，按不同调度频率进行允许
    if s_username == 'jydb':
        json_data['job']['content'][0]['reader']['parameter']['where'] = f"{sync_colname} between to_date('${{start_date}}','yyyymmddhh24miss') and to_date('${{end_date}}','yyyymmddhh24miss')"
        preSql_str = f"delete from {s_username}.{t_tablename} where id in (select recid from jydb.jydb_deleterec where tablename='{t_tablename}' and xgrq between '${{start_date}}' and '${{end_date}}')"
        preSql = []
        preSql.append(preSql_str)
        json_data['job']['content'][0]['writer']['parameter']['preSql'] = preSql
        json_data['job']['content'][0]['writer']['parameter']['writeMode'] = 'replace'
        json_data['job']['content'][0]['writer']['name']='mysqlwriter'
    else:
    # 全量
        if sync_type == 1:
            preSql = []
            preSql_str = f"delete from {t_tablename}"
            preSql.append(preSql_str)
            json_data['job']['content'][0]['writer']['parameter']['preSql'] = preSql
        # 按天
        elif (sync_type in (2,4)):
            if incr_col_type in (1,2):
                json_data['job']['content'][0]['reader']['parameter']['where'] = f"{sync_colname} between to_date('${{start_date}}','yyyymmdd') and to_date('${{end_date}}','yyyymmdd')"
            elif incr_col_type in (3,4):
                json_data['job']['content'][0]['reader']['parameter']['where'] = f"{sync_colname} between '${{start_date}}' and '${{end_date}}'"

            preSql_str = f"delete from {t_tablename} where {sync_colname} between '${{start_date}}' and '${{end_date}}'"
            preSql = []
            preSql.append(preSql_str)
            json_data['job']['content'][0]['writer']['parameter']['preSql'] = preSql
        # 按字段增量
        # elif (sync_type == 3):
        #     json_data['job']['content'][0]['reader']['parameter']['where'] = f"{sync_colname}>'${{{sync_colname}}}'"

    if name=='test':
        with open(f'./output/job/test/{filename}.json', 'w') as file:
            json.dump(json_data, file, indent=4)
    elif name=='product':
        with open(f'./output/job/product/{filename}.json', 'w') as file:
            json.dump(json_data, file, indent=4)
        
def create_table(schema_name,table_name, t_columns):
    # tablename = table_name.lower()
    a = f'create table {schema_name}.{table_name} ({t_columns});'
    with open(f'./output/sql/create_table.sql', 'a') as f:
        f.write(a)
        f.write('\n')


def generate_pre_json_file(table_name, column_name, t_jdbcurl, t_username, t_password,etl_user,etl_password):
    global filename
    with open("./template/oracle2mysql_pre.json", "r") as file:
        json_data = json.load(file)
        json_data['job']['content'][0]['reader']['parameter']['connection'][0]['jdbcUrl'][0] = t_jdbcurl
        querySql = f'SELECT ifnull(max({column_name}),0) FROM {table_name}'
        json_data['job']['content'][0]['reader']['parameter']['connection'][0]['querySql'][0] = querySql

        json_data['job']['content'][0]['writer']['parameter']['fileName'] = f'{filename}_{column_name}'
        json_data['job']['content'][0]['reader']['parameter']['username'] = etl_user
        json_data['job']['content'][0]['reader']['parameter']['password'] = etl_password

    with open(f'./output/job/{filename}_pre.json', 'w') as file:
        json.dump(json_data, file, indent=4)


def collect(name):
    global filename
    conn = pymysql.connect(host="192.168.144.141", user="root", password="IkE==3rB;P5", database="cetl")
    cursor = conn.cursor()
    cursor.execute("select job_id,dbname,tablename,stablename,sjdbc,susername,spassword,sync_type,incr_col,incr_col_type from t_job where status=0 ")
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in results:
        t_dbname = row[1]
        t_tablename = row[2]
        s_tablename = row[3]
        sjdbc = row[4]
        s_username = row[5]
        s_password = row[6]
        sync_type = row[7]
        sync_colname = row[8]
        incr_col_type=row[9]
        t_username = 'rdmetl'
        t_password = 'mysql'
        s_jdbcurl = f'jdbc:oracle:thin:@{sjdbc}'
        t_jdbcurl = f'jdbc:mysql://192.168.144.148:6446/{t_dbname}' 
        dburl = s_jdbcurl.split('@')[-1]
        filename = f'{t_jdbcurl.split('/')[-1]}_{t_tablename}'
        etl_user='rdmetl'
        etl_password='oracle'
        
        if s_username == 'jydb':
            etl_user='jydb'
            etl_password='jydb'

        getColumns(s_username, etl_user,etl_password, dburl,s_tablename)
        if name =='test':
            create_table(t_dbname, t_tablename, create_column_names)
            
        if name=='product':
            if sjdbc=='192.168.146.164/uf':
                sjdbc='10.106.96.204/uf'
            elif sjdbc=='192.168.144.192/cif':
                sjdbc='172.23.15.213/cif'
            elif sjdbc=='192.168.146.118/jydb':
                sjdbc='10.106.96.204/tfdw'
            elif sjdbc=='192.168.144.49/uf':
                # sjdbc='172.23.15.217/orcl'
                sjdbc='10.106.96.130/ufcjk'
                etl_user='tfufcx'
                etl_password='tfufcx'
                
            s_jdbcurl = f'jdbc:oracle:thin:@{sjdbc}'
            t_jdbcurl = f'jdbc:mysql://172.23.15.56:6446/{t_dbname}' 



        generate_json_file(s_jdbcurl, s_tablename, s_username, s_password, t_jdbcurl, t_tablename,t_username, t_password, s_columns_list, t_columns_list, sync_type, sync_colname,incr_col_type,etl_user,etl_password,name)
        if (sync_type == 3):
            generate_pre_json_file(s_tablename, sync_colname, t_jdbcurl, t_username, t_password,etl_user,etl_password)

def distribute(name):
    global filename
    conn = pymysql.connect(host="192.168.144.141", user="root", password="IkE==3rB;P5", database="cetl")
    cursor = conn.cursor()
    cursor.execute("select group_id, dbname,stablename,ttablename,sjdbc,dbtype,ttablename, tjdbc,sync_type,incr_col,incr_col_type,tdbdesc from cetl.t_job2 where status=0")
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in results:
        # t_dbname = row[8]
        t_tablename = row[3]
        s_tablename = row[2]
        sjdbc = row[4]
        s_username = row[1]
        dbtype=row[5]
        etl_user='rdmetl'
        if dbtype=='oracle':
            etl_password='oracle'
            s_password = 'oracle'
        else:
            s_password='mysql'
            etl_password='mysql'
        tjdbc=row[7]    
        sync_type = row[8]
        sync_colname = row[9]
        incr_col_type=row[10]
        tdbdesc=row[11]
        t_username = 'rdmetl'
        t_password = 'mysql'
        s_jdbcurl = f'jdbc:{dbtype}:thin:@{sjdbc}'
        t_jdbcurl = f'jdbc:mysql://{tjdbc}'

        dburl = sjdbc #s_jdbcurl.split('@')[-1]
        filename = f'{tdbdesc}_{t_tablename}'
        if name=='product':
            if sjdbc=='192.168.146.164/uf':
                sjdbc='10.106.96.204/uf'
            elif sjdbc=='192.168.144.192/cif':
                sjdbc='172.23.15.213/cif'
            elif sjdbc=='192.168.146.118/jydb':
                sjdbc='10.106.96.204/tfdw'
            elif sjdbc=='192.168.144.49/uf':
                # sjdbc='172.23.15.217/orcl'
                sjdbc='10.106.96.130/ufcjk'
                etl_user='tfufcx'
                etl_password='tfufcx'
                
            s_jdbcurl = f'jdbc:oracle:thin:@{sjdbc}'
            t_jdbcurl = f'jdbc:mysql://172.23.15.56:6450/dmdw' 
        if dbtype=='oracle':
            getColumns(s_username,etl_user ,etl_password, dburl,s_tablename)
            if name=='test':
                create_table(s_username, t_tablename, create_column_names)
        
        generate_json_file(s_jdbcurl, s_tablename, s_username, s_password, t_jdbcurl, t_tablename,t_username, t_password, s_columns_list, t_columns_list, sync_type, sync_colname,incr_col_type,etl_user,etl_password,name)
        if (sync_type == 3):
            generate_pre_json_file(s_tablename, sync_colname, t_jdbcurl, t_username, t_password)

#main
collect('test')
# collect('product')
# distribute('product')
# distribute('test')