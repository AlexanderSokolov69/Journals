import sys
import sqlite3

from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QTableView, QGridLayout, QLabel, \
    QCheckBox, QFrame, QButtonGroup
from PyQt5 import QtGui, QtCore
from classes.cl_courses import Courses
from classes.cl_group_table import GroupTable
from classes.cl_groups import Groups
from classes.cl_users import Users
from classes.db_session import connectdb
from widgets.checkTable import Ui_tab4Form
from widgets.tab3_form import Ui_tab3Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class tab4FormWindow(QWidget, Ui_tab4Form):
    def __init__(self, con):
        super(tab4FormWindow, self).__init__()
        self.setupUi(self)
        self.initUi(con)

    def initUi(self, con):
        self.chk_buttonGroup = QButtonGroup(self)
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        calend = []
        self.h_layout_table.addWidget(QLabel())
        for day in days:
            calend.append(self.create_day(day))
            self.h_layout_table.addLayout(calend[-1])
#        self.chk_buttonGroup.buttonClicked.connect(self.click)

    def click(self):
        btn : QCheckBox = self.sender()
        print(btn.objectName(), type(btn))
        # if btn.isChecked():
        #     btn.setStyleSheet(f"background-color: rgb(255, 0, 0);")
        # else:
        #     btn.setStyleSheet(f"background-color: rgb(255, 255, 255);")

    def set_time(self, i):
        return f'{8 + i // 2:02}:{i * 30 % 60:02}'

    def create_day(self, day='DAY'):
        kab = [['21', (85, 85, 255)],
               ['22', (255, 0, 0)],
               ['24', (255, 170, 0)],
               ['25', (255, 255, 0)],
               ['27', (196, 0, 127)],
               ['28', (0, 170, 0)]]
        obj = QGridLayout()
        head = QLabel(day)
        head.setAlignment(QtCore.Qt.AlignCenter)
        obj.addWidget(head, 0, 0, 1, 7)
        for i, num in enumerate(kab):
            lbl = QLabel(num[0])
            lbl.setAlignment(QtCore.Qt.AlignCenter)
#            lbl.setStyleSheet(f"background-color: rgb{num[1]};")
            obj.addWidget(lbl, 1, i + 1)
        for i in range(20):
            obj.addWidget(QLabel(self.set_time(i)), i + 2, 0)
            for j, num in enumerate(kab):
                ch_b = QCheckBox(' ')
                ch_b.setObjectName(f"{day} {i} {j}")
                # self.chk_buttonGroup.addButton(ch_b)
                ch_b.stateChanged.connect(self.click)
                ch_b.setStyleSheet(f"background-color: rgb{num[1]};")
                obj.addWidget(ch_b, i + 2, j + 1)
        v_line = QFrame()
        v_line.setFrameShape(QFrame.VLine)
        obj.addWidget(v_line, 0, 7, 22, 7)
        return obj


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    con = sqlite3.connect('..\\db\\database_J.db')
    wnd = tab4FormWindow(con)
    wnd.show()
    sys.exit(app.exec())
