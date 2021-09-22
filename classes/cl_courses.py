from .cl_sqlobject import SQLObject


class Courses(SQLObject):
    def set_sql(self, sql=None, ord='id'):
        self.dbname = 'Courses'
        if sql is None:
            self.sql = f"""select id, name as 'Наименование курса', volume as 'Объем',
                   lesson as 'Урок,(ч)', url as 'Ссылка на сайт', year as 'Учебный год' 
                from courses order by {ord}"""
        else:
            self.sql = f"""{sql} order by {ord}"""
