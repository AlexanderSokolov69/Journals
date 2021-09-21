from sqlite3 import connect
from .qt_classes import MyTableModel

class SQLObject:
    def __init__(self, con: connect):
        if con is None:
            Exception('NO database connection')
        self.cur = con.cursor()
        self.header = []
        self.data = []
        self.tmodel = None
        self.sql = None
        self.set_sql()
        self.update()

    def set_sql(self, sql=None):
        self.sql = sql

    def update(self):
        if self.sql is not None:
            ret = self.cur.execute(self.sql).fetchall()
            self.header = [i[0] for i in self.cur.description]
            self.data = ret
            self.tmodel = MyTableModel(self.header, self.data)
            return len(self.data)
        else:
            return 0

    def model(self):
        return self.tmodel
