import pymysql
conn = pymysql.connect(host="192.168.144.222", user="root", password="IkE==3rB;P5", database="cetl")
cursor = conn.cursor()
cursor.execute("select group_id,group_name from t_group ")
results_group = cursor.fetchall()
job_sql = "select dbname,tablename,incr_col, sync_type  from t_job where group_id=%s order by group_pos,tablename"
content = ''
para_str_day = '''"-Dstart_date=${busi_date} -Dend_date=${busi_date}"'''
common_str1 = "python ../bin/datax.py"
common_str2 = '''
ret_code=$?
if [ $ret_code -gt 0 ];then
    echo `date +'%Y-%m-%d %H:%M:%S'` $busi_date  '''
common_str3 = ''' is error!' >> $LOGFILE
fi
RESULT=$[ $RESULT + $ret_code ]
'''

for row_group in results_group:
    content = ''
    filename = row_group[1]
    cursor.execute(job_sql, (row_group[0]))
    results_job = cursor.fetchall()
    for row in results_job:
        dbname = row[0]
        tablename = row[1]
        incr_col = row[2]
        sync_type = row[3]
        if sync_type == 1:
            tmp_str = f"{common_str1} ./{dbname}/{dbname}_{tablename}.json {common_str2} '{dbname}_{tablename}{common_str3}"
            content = f"{content}\n{tmp_str}"
        elif sync_type == 2:
            tmp_str = f"{common_str1} ./{dbname}/{dbname}_{tablename}.json {para_str_day} {common_str2} '{dbname}_{tablename}{common_str3}"
            content = f"{content}\n{tmp_str}"
        elif sync_type == 3:
            tmp_str = f"""{common_str1} ./{dbname}/{dbname}_{tablename}_pre.json \n{incr_col}=$(cat ./csv/{dbname}_{tablename}_{incr_col}*) \necho '{incr_col}'=${incr_col} \n{common_str1} ./{dbname}/{dbname}_{tablename}.json -p  "-Djsid=${incr_col}"  {common_str2} '{dbname}_{tablename}{common_str3}"""
            content = f"{content}\n{tmp_str}"

    # print(content)
    with open("./template/datax_script_file.sh", "r") as f:
        data = f.read()
        data2 = data.replace('{content}', content)

    with open(f'./output/job/{filename}.sh', 'w') as f:
        f.write(data2)

cursor.close()
conn.close()
