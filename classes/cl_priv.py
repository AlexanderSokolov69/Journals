import sqlite3
from .cl_sqlobject import SQLObject


class Privileges(SQLObject):
    def set_sql(self, sql=None, flt='id'):
        self.keys = (
            ('name', 'Название привилегии доступа:'),
            ('access', 'Код доступа:')
        )
        self.dbname = 'priv'
        if sql is None:
            self.sql = f"""select id, name as 'Наименование', access as "Привилегии"
               from priv
            order by {flt}"""
        else:
            self.sql = f"""{sql} order by {flt}"""
