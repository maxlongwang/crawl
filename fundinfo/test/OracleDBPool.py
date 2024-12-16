import cx_Oracle


class OracleDBPool:
    def __init__(self, dsn, user, password):
        self.pool = cx_Oracle.SessionPool(user=user, password=password, dsn=dsn, increment=1, min=1, max=10)

    def get_conn(self):
        return self.pool.acquire()

    def release_conn(self, conn):
        self.pool.release(conn)

    def close_pool(self):
        self.pool.close()
