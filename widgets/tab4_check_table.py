import sys
import sqlite3

from PyQt5.QtCore import QModelIndex, pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QTableView, QGridLayout, QLabel, \
    QCheckBox, QFrame, QButtonGroup, QSizePolicy, QPushButton, QComboBox, QLineEdit
from PyQt5 import QtGui, QtCore

from classes.bb_converts import get_day_list, get_kab_list, get_time_list
from classes.cl_courses import Courses
from classes.cl_group_table import GroupTable
from classes.cl_groups import Groups
from classes.cl_rasp import Rasp
from classes.cl_users import Users
from classes.db_session import connectdb
from widgets.checkTable import Ui_tab4Form
from widgets.tab3_form import Ui_tab3Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class tab4FormWindow(QWidget, Ui_tab4Form):
    # NUM_SLOTS = 20
    collisium = pyqtSignal()
    LABEL_OK = '----'
    LABEL_FREE = ' ' * 5
    LABEL_COLL = 'XXX'

    def __init__(self, con):
        super(tab4FormWindow, self).__init__()
        self.setupUi(self)
        self.initUi(con)

    def initUi(self, con):
        self.con = con
        self.days_lst = get_day_list(self.con)
        self.kab_lst = get_kab_list(self.con)
        self.time_lst = get_time_list(self.con)
        self.chk_buttonGroup = QButtonGroup(self)
        calend = []
        self.slots_dic = {}
        self.id = -1
        self.current_data = []
        self.edit_widgets = []
        # self.h_layout_table.addWidget(QLabel())
        for nday in range(len(self.days_lst)):
            calend.append(self.create_day(nday))
            self.h_layout_table.addLayout(calend[-1])
#        self.chk_buttonGroup.buttonClicked.connect(self.click)
        self.rasp = Rasp(self.con)
        self.map_table()
        self.tab4_add_btn.clicked.connect(self.group_clicked)
        self.tab4_edit_btn.clicked.connect(self.group_clicked)
        self.tab4_del_btn.clicked.connect(self.group_clicked)
        self.tab4_commit_btn.clicked.connect(self.group_clicked)
        self.tab4_rollback_btn.clicked.connect(self.group_clicked)

    def group_clicked(self):
        btn : QPushButton = self.sender()
        name_btn = btn.objectName()
        if 'commit' in name_btn:
            self.rasp.commit()
            print('commit')
        elif 'rollback' in name_btn:
            self.rasp.rollback()
            print('rollback')
        elif 'add' in name_btn:
            self.id = 0
            self.current_data = []
            self.create_edit_widgets()
            print('add')
        elif 'del' in name_btn:
            for row in [id.row() for id in self.tab4_rasp_view.selectedIndexes() if id.column() == 0]:
                id = self.rasp.data[row][0]
                self.rasp.rec_delete(id)
                print('del', id)
        elif 'edit' in name_btn:
            print('edit')
        self.map_table()

    def showEvent(self, a0):
        self.map_table()
        return super().showEvent(a0)

        # cur = self.con.cursor()
        # for i, val in enumerate(self.time_lst):
        #     sql = f"""insert into times (id, name) values ({i}, "{val}")"""
        #     self.rasp.execute_command(sql)
        # self.rasp.commit()

    def map_table(self):
        self.rasp.update()

        self.tab4_rasp_view.setModel(self.rasp.model())
        self.tab4_rasp_view.resizeColumnsToContents()
        self.tab4_rasp_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        for d, day in enumerate(self.days_lst):
            for k, kab in enumerate(self.kab_lst):
                for t, time in enumerate(self.time_lst):
                    widg : QLabel = self.slots_dic.get(f"{d} {k} {t}", None)
                    if widg:
                        widg.setText(self.LABEL_FREE)
                        widg.setStyleSheet(
                            f"""background-color: rgb(255, 255, 255); font: 12pt "MS Shell Dlg 2";""")
        if not len(self.rasp.data[0]):
        # if self.rasp.data[0][0] is None:
            return
        for rec in self.rasp.data:
            nday = self.days_lst.index(rec[2])
            nkab = -1
            for i, val in enumerate(self.kab_lst):
                if val[0] == rec[3]:
                    nkab = i
            for i, t in enumerate(self.time_lst):
                if rec[4] <= t < rec[5]:
                    widg : QLabel = self.slots_dic.get(f"{nday} {nkab} {i}", None)
                    if widg:
                        if widg.text() == self.LABEL_OK:
                            self.collisium.emit()
                            widg.setText(self.LABEL_COLL)
                        else:
                            widg.setText(self.LABEL_OK)
                        widg.setStyleSheet(
                            f"""background-color: rgb{self.kab_lst[nkab][1]}; font: 12pt "MS Shell Dlg 2";""")

    def click(self):
        btn : QCheckBox = self.sender()
        print(btn.objectName(), type(btn))
        num_day, num_kab, num_time = map(int, btn.objectName().split())
        if btn.isChecked():
            btn.setStyleSheet(f"background-color: rgb{self.kab_lst[num_kab][1]};")
        else:
            btn.setStyleSheet(f"background-color: rgb(255, 255, 255);")

    def create_day(self, day=0):
        obj = QGridLayout()
        obj.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        head = QLabel(self.days_lst[day])
        head.setAlignment(QtCore.Qt.AlignCenter)
        obj.addWidget(head, 0, 0, 1, 7)
        for i, num in enumerate(self.kab_lst):
            lbl = QLabel(f" {num[0]} ")
            lbl.setStyleSheet(f'background-color: rgb{num[1]}; font: 12pt "MS Shell Dlg 2";')
            # lbl.setStyleSheet('font: 12pt "MS Shell Dlg 2";')
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            sizePolicy.setHeightForWidth(lbl.sizePolicy().hasHeightForWidth())
            lbl.setSizePolicy(sizePolicy)
#            lbl.setStyleSheet(f"background-color: rgb{num[1]};")
            obj.addWidget(lbl, 1, i + 1)
        for i in range(len(self.time_lst)):
            lbl = QLabel(f"{self.time_lst[i]} ")
            lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            sizePolicy.setHeightForWidth(lbl.sizePolicy().hasHeightForWidth())
            lbl.setSizePolicy(sizePolicy)
            obj.addWidget(lbl, i + 2, 0)
            for j, num in enumerate(self.kab_lst):
                # ch_b = QCheckBox(' ')
                ch_b = QLabel('')
                ch_b.setAlignment(QtCore.Qt.AlignCenter)
                ch_b.setObjectName(f"{day} {j} {i}")
                ch_b.setStyleSheet(f"""background-color: rgb(255, 255, 255);  font: 12pt "MS Shell Dlg 2";""")
                sizePolicy.setHeightForWidth(ch_b.sizePolicy().hasHeightForWidth())
                ch_b.setSizePolicy(sizePolicy)
                self.slots_dic[ch_b.objectName()] = ch_b
                obj.addWidget(ch_b, i + 2, j + 1)
        v_line = QFrame()
        v_line.setFrameShape(QFrame.VLine)
        obj.addWidget(v_line, 0, len(self.kab_lst) + 1, 22, len(self.kab_lst) + 1)
        return obj

    def delete_edit_form(self, curLayout):
        """ Удаляем поля редактирования """
        for widg in self.edit_widgets:
            curLayout.removeWidget(widg)
            widg.deleteLater()
        self.edit_widgets.clear()

    def create_edit_widgets(self):
        curLayout = self.tab4_edit_layout
        """ Создание полей редактирования записи """
        self.current_data = self.rasp.get_record(self.id)
        self.delete_edit_form(curLayout)
        lrow = 0
        sP = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        # sP.setHorizontalStretch(0)
        # sP.setVerticalStretch(0)
        lP = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # lP.setHorizontalStretch(0)
        # lP.setVerticalStretch(0)
        # sP.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        for i, val in enumerate(self.current_data):
            self.edit_widgets.append(QLabel(val[1], self))
            curLayout.addWidget(self.edit_widgets[-1], i, 0)
            self.edit_widgets[-1].setSizePolicy(lP)
            if val[0][:2] == 'id':
                self.edit_widgets.append(QComboBox(self))
                self.edit_widgets[-1].setDisabled(False)
                self.edit_widgets[-1].setSizePolicy(sP)
                self.edit_widgets[-1].setFocusPolicy(Qt.StrongFocus)
                curLayout.addWidget(self.edit_widgets[-1], i, 1)
                if val[0][2:] == 'Groups':
                    sql = f"""select id || " : " || name from {val[0][2:]} order by name"""
                else:
                    sql = f"""select id || " : " || name from {val[0][2:]}"""
                # sql = f"select name from {val[0][2:]}"
                cur = self.con.cursor()
                spis = cur.execute(sql).fetchall()
                self.edit_widgets[-1].addItems([val[:][0] for val in spis])
                for i in range(self.edit_widgets[-1].count()):
                    fnd = self.edit_widgets[-1].itemText(i)
                    id = fnd[:fnd.find(':') - 1]
                    if id == str(val[2]):
                        self.edit_widgets[-1].setCurrentIndex(i)
                print(self.edit_widgets[-1].count())
            else:
                le = QLineEdit(str(val[2]), self)
                if val[0][:] in ['start', 'end']:
                    le.setInputMask('99:99')
                    # le.textChanged.connect(self.control_time)
                # elif val[0][:] in 'end':
                #     le.setReadOnly(True)
                self.edit_widgets.append(le)
                curLayout.addWidget(self.edit_widgets[-1], i, 1)
                self.edit_widgets[-1].setSizePolicy(sP)
            self.edit_widgets[1].setFocus()
            lrow = i
        pbS = QPushButton('Применить')
        pbS.setSizePolicy(sP)
        curLayout.addWidget(pbS, 4, 2)
        pbC = QPushButton('Отменить')
        pbC.setSizePolicy(sP)
        curLayout.addWidget(pbC, 5, 2)
        curLayout.addWidget(QFrame(), 0, 3, lrow, 3)

    def control_time(self):
        print('corr')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    con = sqlite3.connect('..\\db\\database_J.db')
#    con = sqlite3.connect('O:/Журналы/db/database_J.db')
    wnd = tab4FormWindow(con)
    wnd.show()
    sys.exit(app.exec())
