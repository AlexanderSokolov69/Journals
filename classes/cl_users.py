import sqlite3
from .cl_sqlobject import SQLObject


class Users(SQLObject):
    def set_sql(self, sql=None, flt='Фамилия'):
        self.editable = True
        self.keys = (
            ('name', 'Фамилия И.О.:'),
            ('fam', 'Фамилия:'),
            ('ima', 'Имя:'),
            ('otch', 'Отчество:'),
            ('login', 'Логин для входа в программу:'),
            ('phone', 'Номер телефона:'),
            ('email', 'e-mail адрес:'),
            ('birthday', 'Дата рождения:'),
            ('idRoles', 'Роль доступа:'),
            ('idPlaces', 'Место работы/учёбы:'),
            ('comment', 'Дополнительная информация:'),
            ('sertificate', 'Сертификат ПФДО:')
        )
        self.dbname = 'users'
        if sql is None:
            self.sql = f"""select u.id, u.name as 'Фамилия И.О.', u.fam as "Фамилия", u.ima as 'Имя', 
                u.otch as 'Отчество', u.login as 'Логин', u.phone as 'Телефон', 
                u.email as 'E-mail', u.birthday as 'Д.рожд', u.sertificate as 'Сертификат ПФДО',
                r.name as 'Роль', p.name as 'Место учёбы/работы', p.comment as 'Класс/Должн.',
                u.comment as 'Доп.информация'
               from users u
               join roles r on u.idRoles = r.id
               join places p on u.idPlaces = p.id 
               order by {flt}"""
        else:
            self.sql = f"""{sql} order by {flt}"""

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
