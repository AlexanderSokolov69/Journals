from .cl_sqlobject import SQLObject


class Groups(SQLObject):
    def get_all(self, ord='course'):
        sql = f"""select g.id, g.name as "group", c.name as "course", c.volume, c.lesson, c.year, 
                u.fam, u.name, u.sname  from groups g
            join users u on g.teacher = u.id
            join courses c on g.idCourse = c.id
        order by {ord}"""
        return super()._get(sql)
