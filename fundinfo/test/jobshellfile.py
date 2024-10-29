import pymysql
from textwrap import dedent
def jobshell(direction):

    conn = pymysql.connect(host="192.168.144.141", user="root", password="IkE==3rB;P5", database="cetl")
    cursor = conn.cursor()
    cursor.execute("select group_id,group_name from t_group")
    results_group = cursor.fetchall()
    if direction==1:
        job_sql = "select dbname,tablename,incr_col, sync_type,incr_col_type  from t_job t1 join t_group_job t2 on t1.job_id =t2.job_id where t2.group_id=%s  order by t1.create_date,tablename"
    elif direction==2:
        job_sql = "select tdbdesc  dbname,ttablename tablename,incr_col, sync_type,incr_col_type  from cetl.t_job2 where group_id=%s order by create_date,ttablename"
        
    content = ''

    common_str1 = "python ../bin/datax.py"
    common_str2 = '''\nret_code=$? \nif [ $ret_code -gt 0 ];then \n  echo `date +'%Y-%m-%d %H:%M:%S'` $busi_date'''
    common_str3 = ''' is error!' >> $LOGFILE \nfi \nRESULT=$[ $RESULT + $ret_code ]  \n'''


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
            incr_col_type=row[4]
            if dbname=='jydb':
                para_str_day = '"-Dstart_date=$start_time -Dend_date=$end_time"'
                tmp_str = f"{common_str1} ./{dbname}/{dbname}_{tablename}.json -p {para_str_day} {common_str2} '{dbname}_{tablename}{common_str3}"
                content = f"{content}\n{tmp_str}"
            else:
                if sync_type == 1:
                    tmp_str = f"{common_str1} ./{dbname}/{dbname}_{tablename}.json {common_str2} '{dbname}_{tablename}{common_str3}"
                    content = f"{content}\n{tmp_str}"
                elif sync_type == 2:
                    if incr_col_type ==4:
                        para_str_day = '"-Dstart_date=$month_date -Dend_date=$month_date"'
                    elif incr_col_type ==2:
                        para_str_day = '"-Dstart_date=$start_date -Dend_date=$end_date2"'
                    else:
                        para_str_day = '"-Dstart_date=$start_date -Dend_date=$end_date"'
                    tmp_str = f"{common_str1} ./{dbname}/{dbname}_{tablename}.json -p {para_str_day} {common_str2} '{dbname}_{tablename}{common_str3}"
                    content = f"{content}\n{tmp_str}"
                elif sync_type == 4:
                    para_str_day = '"-Dstart_date=$quarter -Dend_date=$quarter"'
                    tmp_str = f"{common_str1} ./{dbname}/{dbname}_{tablename}.json -p {para_str_day} {common_str2} '{dbname}_{tablename}{common_str3}"
                    content = f"{content}\n{tmp_str}"
                    
                elif sync_type == 3:
                    tmp_str = f"""{common_str1} ./{dbname}/{dbname}_{tablename}_pre.json \n{incr_col}=$(cat ./csv/{dbname}_{tablename}_{incr_col}*) \necho '{incr_col}'=${incr_col} \n{common_str1} ./{dbname}/{dbname}_{tablename}.json -p  "-Djsid=${incr_col}"  {common_str2} '{dbname}_{tablename}{common_str3}"""
                    content = f"{content}\n{tmp_str}"

        # print(content)
        with open("./template/datax_script_file.sh", "r") as f:
            data = f.read()
            data2 = data.replace('{content}', content)

        with open(f'./output/script/{filename}.sh', 'w') as f:
            f.write(data2)

    cursor.close()
    conn.close()
# 1 collect 2 distribute
# jobshell(1)
jobshell(2)