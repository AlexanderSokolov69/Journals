import sqlite3

class Logger:
    def __init__(self, con):
        self.con = con
        self.cur = con.cursor()
        self.sql = "insert into log (id, fio, date, time, info) values (?, ?, ?, ?, ?)"

    def out(self, arg):
        self.cur.execute(self.sql, arg)
        self.con.commit()

if __name__ == '__main__':
    con = sqlite3.connect('..\\db\\database_J.db')
    lg = Logger(con)
    [lg.out(('1', '2', '3', '4', '5')) for _ in range(10)]
    con.commit()