from .db_session import connectdb
from .cl_sqlobject import SQLObject


class Users(SQLObject):
    def set_sql(self, sql=None, ord='Фамилия'):
        if sql is None:
            self.sql = f"""select u.id, u.fio as 'Фамилия И.О.', u.fam as "Фамилия", u.name as 'Имя', 
                u.sname as 'Отчество', u.birthday as 'Д.рожд', u.phone as 'Телефон', u.email as 'E-mail', 
                u.comment as 'Доп.информация', r.name as 'Роль', p.name as 'Профессия', p.comment as 'Доп.инфо' 
               from users u
               join roles r on u.idRole = r.id
               join places p on u.idPlace = p.id order by {ord}"""
        else:
            self.sql = f"""{sql} order by {ord}"""


if __name__ == '__main__':
    con = connectdb('..\\db.database_J.db')
    print(Users(con))
