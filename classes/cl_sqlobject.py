import sqlite3
from sqlite3 import connect
from .qt_classes import MyTableModel

class SQLObject:
    def __init__(self, con: connect):
        if con is None:
            Exception('NO database connection')
        self.con : sqlite3.connect = con
        self.cur = con.cursor()
        self.header = []
        self.data = []
        self.tmodel = None
        self.sql = None
        self.set_sql()
        self.update()
        self.dbname = None
        self.keys = []

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

    def commit(self):
        self.con.commit()

    def rollback(self):
        self.con.rollback()

    def rec_update(self, id, arg: dict):
        args = ', '.join([f'{item[0]} = "{item[1]}"' for item in arg.items()])
        sql = f"update {self.dbname} set {args} where id = {id}"
        print(sql)
        self.cur.execute(sql)
        return True

    def rec_append(self, arg: dict):
        key = ', '.join(arg.keys())
        val = f""" "{'", "'.join(arg.values())}" """
        sql = f"insert into {self.dbname} ({key}) values ({val})"
        print(sql)
        self.cur.execute(sql)
        return True

    def rec_delete(self, id):
        sql = f"delete from {self.dbname} where id = {id}"
        self.cur.execute(sql)
        return True


if __name__ == '__main__':
    pass