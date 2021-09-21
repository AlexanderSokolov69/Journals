from .cl_sqlobject import SQLObject


class Groups(SQLObject):
    def set_sql(self, sql=None, ord='g.id'):
        if sql is None:
            self.sql = f"""select g.id, g.name as "Группа", c.name as "Учебный курс", c.volume as "Объем", 
                    c.lesson as "Занятие", c.year as "Уч.год", u.fio as "ФИО наставника" 
                from groups g
                join users u on g.teacher = u.id
                join courses c on g.idCourse = c.id
            order by {ord}"""
        else:
            self.sql = f"""{sql} order by {ord}"""
