import sqlite3
from .cl_sqlobject import SQLObject


class Places(SQLObject):
    def set_sql(self, sql=None, flt='Наименование'):
        self.keys = (
            ('name', 'Место работы/учёбы:'),
            ('comment', 'класс/доп.инф.:')
        )
        self.dbname = 'places'
        if sql is None:
            self.sql = f"""select id, name as 'Наименование', comment as "Доп.инфо"
               from places
            order by {flt}"""
        else:
            self.sql = f"""{sql} order by {flt}"""
