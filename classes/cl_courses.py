from .cl_sqlobject import SQLObject


class Courses(SQLObject):
    def set_sql(self, sql=None, ord='year, name'):
        if sql is None:
            self.sql = f'select * from courses order by {ord}'
        else:
            self.sql = f"""{sql} order by {ord}"""
