from .cl_sqlobject import SQLObject


class Groups(SQLObject):
    def set_sql(self, sql=None, flt='g.id'):
        self.keys = (
            ('name', 'Кодовое название учебной группы:'),
            ('idCourses', 'Учебная программа:'),
            ('idUsers', 'Фамилия И.О. наставника:')
        )
        self.dbname = 'groups'
        if sql is None:
            self.sql = f"""select g.id, g.name as "Группа", c.name as "Учебный курс", c.volume as "Объем", 
                    c.lesson as "Занятие", c.year as "Уч.год", u.name as "ФИО наставника" 
                from groups g
                join users u on g.idUsers = u.id
                join courses c on g.idCourses = c.id
            order by {flt}"""
        else:
            self.sql = f"""{sql} order by {flt}"""
