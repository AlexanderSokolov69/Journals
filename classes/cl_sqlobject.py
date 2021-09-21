from sqlite3 import connect

class SQLObject:
    def __init__(self, con: connect):
        if con is None:
            Exception('NO database connection')
        self.cur = con.cursor()

    def _get(self, sql):
        ret = self.cur.execute(sql).fetchall()
        return [i[0] for i in self.cur.description], ret
