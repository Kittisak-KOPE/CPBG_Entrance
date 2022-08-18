import psycopg2

class databasepq():
    def __init__(self,**connect):
        self.conn = psycopg2.connect(**connect)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def execute(self, query, stm):
        self.cur.execute(query, stm)

    def fetchAll(self):
        return self.cur.fetchall()

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
