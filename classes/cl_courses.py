from .cl_sqlobject import SQLObject


class Courses(SQLObject):
    def set_sql(self, sql=None, flt='id'):
        self.keys = (
            ('name', 'Наименование учебного курса:'),
            ('target', 'Возрастная группа:'),
            ('volume', 'Объём курса в акк.часах:'),
            ('lesson', 'Продолжительность занятия, акк.ч.:'),
            ('url', 'Ссылка на раздел на сайте:'),
            ('year', 'Учебный год:')
        )
        self.dbname = 'Courses'
        if sql is None:
            self.sql = f"""select id, name as 'Наименование курса', target as 'Возраст', volume as 'Объем',
                   lesson as 'Урок,(ч)', url as 'Ссылка на сайт', year as 'Учебный год' 
                from courses order by {flt}"""
        else:
            self.sql = f"""{sql} order by {flt}"""


