import sqlite3
from .cl_sqlobject import SQLObject


class Privileges(SQLObject):
    def set_sql(self, sql=None, ord='id'):
        self.dbname = 'priv'
        if sql is None:
            self.sql = f"""select id, name as 'Наименование', access as "Привилегии"
               from priv
            order by {ord}"""
        else:
            self.sql = f"""{sql} order by {ord}"""
