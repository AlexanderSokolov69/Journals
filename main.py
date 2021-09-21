from classes.db_session import connectdb
from classes.db_classes import Users, Courses, Groups
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 1200, 400)
        con = connectdb('db\\database_J.db')
        spis = Users(con).get_all()
        print(spis)

    #    self.tbl.horizontalHeader(0).setText(spis[0][0])
     #   [self.tbl.horizontalHeader(i).setText(spis[0][i]) for i in range(len(spis[0]))]
        self.adjustSize()
        self.show()


def main():
    con = connectdb('db\\database_J.db')
    print(Users(con).get_all())
    # cur = con.cursor()
    # result = cur.execute('select * from users').fetchall()
    # print(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    sys.exit(app.exec())

