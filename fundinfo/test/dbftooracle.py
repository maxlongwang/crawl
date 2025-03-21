import cx_Oracle
from dbfread import DBF
from collections import OrderedDict

file_path = r'D:\tfzq\info_check\qtzhzl100091.228'
table_name = 'reader.qtzhzl'
BatchSize = 5000
conn = cx_Oracle.connect('system', 'oracle', '192.168.144.74/eif')
cursor = conn.cursor()

def read_data(file_path):
    dbf=DBF(filename=file_path, encoding='gbk')
    for record in dbf:
        print(record)

def read_dat(file_path):
    dbf = DBF(filename=file_path, encoding='gbk')
    columns = dbf.field_names
    placeholders = ':'+",:".join(str(i+1) for i in range(len(columns)))
    sql = f"insert into {table_name}({', '.join(columns)}) values ({placeholders})"
    rows = []
    for record in dbf:
        rows.append(tuple(record.values()))
        if len(rows) % BatchSize == 0:
            batchSave(sql=sql, rows=rows)
            rows.clear()
    if rows:
        batchSave(sql=sql, rows=rows)


def batchSave(sql, rows):
    cursor.executemany(sql, rows)
    conn.commit()


if __name__ == "__main__":
    # read_data(file_path=file_path)
    read_dat(file_path=file_path)
    cursor.close()
    conn.close()
