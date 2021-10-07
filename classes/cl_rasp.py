from .cl_sqlobject import SQLObject


class Rasp(SQLObject):
    def set_sql(self, sql=None, flt='g.id'):
        self.keys = (
            ('idGroups', 'Учебная группа:'),
            ('idDays', 'День недели'),
            ('idKabs', 'Кабинет:'),
            ('start', 'Начало занятий:'),
            ('end', 'Окончание занятий:'),
            ('comment', 'Доп. информация')
        )
        self.dbname = 'groups'
        if sql is None:
            self.sql = f"""select r.id, g.name || " - " || ju.name as "Группа - наставник", d.name as "День недели" , 
                    k.name as "Кабинет", r.start as "Начало", r.end as "Окончание", 
                    jc.acchour as "Акк. час", jc.hday as "Занятий в день", r.comment as "Доп. информация"
                from rasp r
                join kabs k on r.idKabs = k.id
                join days d on r.idDays = d.id
                join groups g on r.idGroups = g.id
                join (select gu.id, u.name from groups gu join users u on gu.idUsers = u.id) ju on ju.id = g.id
                join (select cu.id, cu.acchour, cu.hday from courses cu) jc on jc.id = g.idCourses
            order by {flt}"""
        else:
            self.sql = f"""{sql} order by {flt}"""
