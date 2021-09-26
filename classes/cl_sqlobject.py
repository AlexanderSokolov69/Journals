import sqlite3
from sqlite3 import connect
from .qt_classes import MyTableModel
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
        # self.log = Logger(con)

    def set_sql(self, sql=None, flt=None):
        pass

    def update(self):
        if self.sql is not None:
            try:
                ret = self.cur.execute(self.sql).fetchall()
            except (sqlite3.Error, sqlite3.Warning) as err:
                # self.log.out(str(datetime.date), str(datetime.time), '[update class]', str(err), self.sql)
                print(err, '[update class]', self.sql)
                ret = None
            if ret:
                self.header = [i[0] for i in self.cur.description]
                self.data = [['' if zp == None else zp for zp in rec] for rec in ret]
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
        try:
            self.con.commit()
        except (sqlite3.Error, sqlite3.Warning) as err:
            # self.log.out(str(datetime.date), str(datetime.time), '[commit]', str(err), '')
            print(err, '[commit]')

    def rollback(self):
        try:
            self.con.rollback()
        except (sqlite3.Error, sqlite3.Warning) as err:
            # self.log.out(str(datetime.date), str(datetime.time), '[rollback]', str(err), '')
            print(err, '[rollback]')

    def rec_update(self, id, arg: dict):
        args = ', '.join([f'{item[0]} = "{item[1]}"' for item in arg.items()])
        sql = f"update {self.dbname} set {args} where id = {id}"
        try:
            self.cur.execute(sql)
        except (sqlite3.Error, sqlite3.Warning) as err:
            # self.log.out(str(datetime.date), str(datetime.time), '[update record]', str(err), self.sql)
            print(err, '[update record]', sql)
        return True

    def rec_append(self, arg: dict):
        key = ', '.join(arg.keys())
        val = '"' + '", "'.join(arg.values()) +'"'
        sql = f"""insert into {self.dbname} ({key}) values ({val})"""
        try:
            self.cur.execute(sql)
        except (sqlite3.Error, sqlite3.Warning) as err:
            # self.log.out(str(datetime.date), str(datetime.time), '[append record]', str(err), self.sql)
            print(err, '[append record]', sql)
        return True

    def rec_delete(self, id):
        sql = f"delete from {self.dbname} where id = {id}"
        try:
            self.cur.execute(sql)
        except (sqlite3.Error, sqlite3.Warning) as err:
            # self.log.out(str(datetime.date), str(datetime.time), '[delete record]', str(err), self.sql)
            print(err, '[delete record]', sql)
        return True

    def get_record(self, id):
        fields = ', '.join([key[0] for key in self.keys])
        sql = f"select {fields} from {self.dbname} where id = {id}"
        cur = self.con.cursor()
        data = None
        try:
            data = cur.execute(sql).fetchone()
        except (sqlite3.Error, sqlite3.Warning) as err:
            # self.log.out(str(datetime.date), str(datetime.time), '[get record]', str(err), self.sql)
            print(err, '[get record]', sql)
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
        try:
            ret = cur.execute(comm).fetchall()
        except (sqlite3.Error, sqlite3.Warning) as err:
            # self.log.out(str(datetime.date), str(datetime.time), '[execute command]', str(err), self.sql)
            print(err, '[execute command]', comm)
            ret = [[]]
        return ret


if __name__ == '__main__':
    pass