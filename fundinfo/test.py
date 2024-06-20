
import pandas as pd

df = pd.read_excel('table_oracle2mysql.xlsx')
# print(df.head())
for _,row in df.iterrows():
    s_tablename=row['s_tablename']
    s_jdburl=row['s_jdbcurl']
    s_username=row['s_jdbcurl']
    s_password=row['s_jdbcurl']
    t_tablename=row['s_jdbcurl']
    t_jdbcurl=row['s_jdbcurl']
    t_username=row['s_jdbcurl']
    t_password=row['t_password']

    
    