

import os
import cx_Oracle

PATH = 'D:/my/music'

conn = cx_Oracle.connect('system', 'oracle', '192.168.144.66/eif')
cursor = conn.cursor()


def get_filenames():
    items = os.listdir(PATH)
    for item in items:
        file_name = item
        update_status(file_name=file_name)


def update_status(file_name):
    sql = f"update scott.t_pandamusic set status=1 where file_name='{file_name}'"
    print(sql)
    cursor.execute(sql)


if __name__ == "__main__":
    get_filenames()
    conn.commit()

    cursor.close()
    conn.close()
