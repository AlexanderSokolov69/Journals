from .cl_sqlobject import SQLObject


class GroupTable(SQLObject):
    def set_sql(self, sql=None, ord='id'):
        self.dbname = 'group_table'
        if sql is None:
            self.sql = f"""select t.id as 'id', g.name as "Группа", u.fio as "Фамилия И.О.", 
                    t.comment as "Комментарий" 
                from group_table t
                join groups g on g.id = t.idGroup
                join users u on u.id = t.idUser
            order by {ord}"""
        else:
            self.sql = f"""{sql} order by {ord}"""
