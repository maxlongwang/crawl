import cx_Oracle
import json
import pandas as pd

create_column_names = ''
s_columns_list = []
t_columns_list = []


def getColumns(s_username, s_password, dburl):
    global create_column_names, s_columns_list, t_columns_list
    conn = cx_Oracle.connect(s_username, s_password, dburl)
    cursor = conn.cursor()
    sql = f'''
        select column_name,
                data_type2 || case
                        when data_type = 'NUMBER' then
                        '(' || data_length || ',4)'
                        when data_type in ('CHAR', 'VARCHAR2') then
                        '(' || data_length || ')'
                    end data_type3
        from (select column_name,
                        data_type,
                        data_precision,
                        case
                        when data_type = 'VARCHAR2' then
                        'VARCHAR'
                        when data_type = 'NUMBER' then
                        'DECIMAL'
                        when data_type = 'DATE' then
                        'DATETIME'
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


def generate_json_file(s_jdbcurl, s_tablename, s_username, s_password, t_jdbcurl, t_tablename, t_username, t_password, s_columns_list, t_columns_list):
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

    with open(f'./output/json/{s_tablename}_oracle2mysql.json', 'w') as file:
        json.dump(json_data, file, indent=4)


def create_table(table_name, t_columns):
    # tablename = table_name.lower()
    a = f'create table {table_name} ({t_columns})'
    with open(f'./output/sql/{table_name}.sql', 'w') as f:
        f.write(a)


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

    dburl = s_jdbcurl.split('@')[-1]

    getColumns(s_username, s_password, dburl)
    generate_json_file(s_jdbcurl, s_tablename, s_username, s_password, t_jdbcurl, t_tablename, t_username, t_password, s_columns_list, t_columns_list)
    create_table(t_tablename, create_column_names)
