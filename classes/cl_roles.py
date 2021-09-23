import sqlite3
from .cl_sqlobject import SQLObject


class Roles(SQLObject):
    def set_sql(self, sql=None, ord='id'):
        self.keys = (
            ('name', 'Роль пользователя:'),
            ('idPriv', 'Привилегия доступа:')
        )
        self.dbname = 'roles'
        if sql is None:
            self.sql = f"""select r.id as 'id', r.name as 'Наименование', p.name as "Привилегии"
               from roles r
               join priv p on p.id = r.idPriv
            order by {ord}"""
        else:
            self.sql = f"""{sql} order by {ord}"""
