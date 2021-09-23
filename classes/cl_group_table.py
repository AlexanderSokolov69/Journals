from .cl_sqlobject import SQLObject


class GroupTable(SQLObject):
    def set_sql(self, sql=None, flt='id'):
        self.keys = (
            ('idGroups', 'Учебная группа:'),
            ('idUsers', 'Фамилия И.О. кубиста:'),
            ('comment', 'Дополнительная информация:')
        )
        self.dbname = 'group_table'
        if sql is None:
            self.sql = f"""select t.id as 'id', g.name as "Группа", u.name as "Фамилия И.О.", 
                    t.comment as "Комментарий" 
                from group_table t
                join groups g on g.id = t.idGroups
                join users u on u.id = t.idUsers
            order by {flt}"""
        else:
            self.sql = f"""{sql} order by {flt}"""
