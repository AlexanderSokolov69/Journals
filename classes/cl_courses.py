from .cl_sqlobject import SQLObject


class Courses(SQLObject):
    def get_all(self, ord='year, name'):
        sql = f'select * from courses order by {ord}'
        return super()._get(sql)
