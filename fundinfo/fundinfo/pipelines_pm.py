from itemadapter import ItemAdapter
import cx_Oracle
import datetime
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# def _getconnect():
#     conn=cx_Oracle.connect('reader', 'reader', '192.168.144.66/eif')
#     return conn

class PandaMusicPipeline:
    def __init__(self):
        self.conn = cx_Oracle.connect('system', 'oracle', '192.168.144.66/eif')
        self.cursor = self.conn.cursor()
        self.data = []
        self.insert_sql = None
        self.table_name = 'scott.t_pandamusic'

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.cursor.close()
        self.conn.close()
        

    def process_item(self, item, spider):
        if not self.insert_sql:
            col_names = (dict(item).keys())
            placeholders = placeholders = ', '.join([':' + str(i + 1) for i in range(len(col_names))])
            self.insert_sql = (
                f"INSERT INTO {self.table_name}({','.join(col_names)}) "
                f"VALUES ({placeholders})"
            )

        page_data = tuple(dict(item).values())
        self.data.append(page_data)

        if len(self.data) >0:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(self.insert_sql, self.data)
        self.conn.commit()
