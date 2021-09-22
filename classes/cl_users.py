import sqlite3
from .cl_sqlobject import SQLObject
from .cl_password import Password


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

    def get_user_login(self, login):
        sql = f'select * from users where login = "{login.lower()}"'
        cur = self.con.cursor()
        data = cur.execute(sql).fetchone()
        if data:
            ret = {}
            for i, key in enumerate(cur.description):
                ret[key[0]] = data[i]
        else:
            ret = None
        return ret

    def set_user_password(self, id, passwd):
        sql = f"update users set passwd = ? where id = {id}"
        cur = self.con.cursor()
        cur.execute(sql, [passwd])
        self.con.commit()

if __name__ == '__main__':
    con = sqlite3.connect('..\\db\\database_J.db')
    us = Users(con)
    print(us.get_user_login('falcon'))
