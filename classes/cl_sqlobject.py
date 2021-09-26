import sqlite3
from sqlite3 import connect

from .qt_classes import MyTableModel
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject


class SQLObject(QObject):
    need_to_save = pyqtSignal()
    def __init__(self, con: connect):
        super(SQLObject, self).__init__()
        if con is None:
            Exception('NO database connection')
        # self.need_save = pyqtSignal()
        self.con : sqlite3.connect = con
        self.cur = con.cursor()
        self.tmodel = None
        self.sql = None
        self.dbname = None
        self.header = []
        self.data = []
        self.keys = []
        self.editable = False
        self.set_sql()
        self.update()

    def set_sql(self, sql=None, flt=None):
        pass

    def update(self):
        if self.sql is not None:
            ret = self.cur.execute(self.sql).fetchall()
            if ret:
                self.header = [i[0] for i in self.cur.description]
                self.data = [list(rec) for rec in ret]
            else:
                self.data =[[]]
            self.tmodel = MyTableModel(self.header, self.data, self.editable)
            self.tmodel.need_save.connect(self.update_model)
            return len(self.data)
        else:
            return 0

    def update_model(self):
        self.rec_update(self.data[self.tmodel.current_index[0]][0],
                        {self.keys[self.tmodel.current_index[1] - 1][0]:
                             self.data[self.tmodel.current_index[0]][self.tmodel.current_index[1]]}
                        )
        self.need_to_save.emit()

    def model(self):
        return self.tmodel

    def commit(self):
        self.con.commit()

    def rollback(self):
        self.con.rollback()

    def rec_update(self, id, arg: dict):
        args = ', '.join([f'{item[0]} = "{item[1]}"' for item in arg.items()])
        sql = f"update {self.dbname} set {args} where id = {id}"
        self.cur.execute(sql)
        return True

    def rec_append(self, arg: dict):
        key = ', '.join(arg.keys())
        val = '"' + '", "'.join(arg.values()) +'"'
        sql = f"""insert into {self.dbname} ({key}) values ({val})"""
        self.cur.execute(sql)
        return True

    def rec_delete(self, id):
        sql = f"delete from {self.dbname} where id = {id}"
        self.cur.execute(sql)
        return True

    def get_record(self, id):
        fields = ', '.join([key[0] for key in self.keys])
        sql = f"select {fields} from {self.dbname} where id = {id}"
        cur = self.con.cursor()
        data = cur.execute(sql).fetchone()
        if not data:
            data = [''] * len(self.keys)
        ret = []
        for i, key in enumerate(self.keys):
            key = list(key)
            key.append(data[i])
            ret.append(key)
        return ret

    def execute_command(self, comm):
        cur = self.con.cursor()
        ret = cur.execute(comm).fetchall()
        return ret



if __name__ == '__main__':
    pass