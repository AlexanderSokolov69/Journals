import PyQt5
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QAbstractItemView, QPushButton

from classes.db_classes import Privileges, Roles, Places, Courses, GroupTable, Groups
from widgets.MainWindow import Ui_MainWindow
from classes.cl_sqlobject import SQLObject


class MWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, con):
        super(MWindow, self).__init__()
        self.setupUi(self)
        self.initUi(con)

    def initUi(self, con):
        self.setWindowTitle('IT-куб. Белая Холуница. Журналы. v.0.9')
        self.con = con
        self.table_list = {
            0: ('Привилегии доступа', Privileges(self.con)),
            1: ('Роли пользователей', Roles(self.con)),
            2: ('Места работы/учёбы', Places(self.con)),
            3: ('Учебные программы', Courses(self.con)),
            4: ('Учебные группы', Groups(self.con)),
            5: ('Списки учебных групп', GroupTable(self.con))
        }

        self.currTable  : SQLObject = None
        self.listBox.addItems([val[0] for val in self.table_list.values()])
        self.listBox.currentIndexChanged.connect(self.change_table)
        self.listBox.setCurrentIndex(3)

        # Фильтр списка
        self.fltCheck.stateChanged.connect(self.filter)
        self.fltCheck.setChecked(True)
        self.fltCheck.setChecked(False)

        self.addButton.clicked.connect(self.add_record)
        self.editButton.clicked.connect(self.edit_record)
        self.delButton.clicked.connect(self.del_record)
        self.commitButton.clicked.connect(self.refresh_table)
        self.rollbackButton.clicked.connect(self.refresh_table)

    def refresh_table(self):
        if type(self.sender()) == PyQt5.QtWidgets.QPushButton:
            if self.sender().text() == self.commitButton.text():
                self.currTable.commit()
            elif self.sender().text() == self.rollbackButton.text():
                self.currTable.rollback()
        self.currTable.update()
        self.tableView.setModel(self.currTable.model())
        self.tableView.resizeColumnsToContents()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        if self.currTable.con.in_transaction:
            self.transLabel.setText('')
            self.commitButton.setFlat(False)
            self.rollbackButton.setFlat(False)
            self.commitButton.setDisabled(False)
            self.rollbackButton.setDisabled(False)
        else:
            self.transLabel.setText('')
            self.commitButton.setFlat(True)
            self.rollbackButton.setFlat(True)
            self.commitButton.setDisabled(True)
            self.rollbackButton.setDisabled(True)

    def add_record(self):
        self.currTable.rec_append({'name': 'Пример'})
        self.refresh_table()

    def del_record(self):
        self.currTable.rec_delete(self.currTable.data[self.tableView.currentIndex().row()][0])
        self.refresh_table()

    def edit_record(self):
        id = self.currTable.data[self.tableView.currentIndex().row()][0]
        val = self.currTable.data[self.tableView.currentIndex().row()]
        data = {}
        for i, key in enumerate(self.currTable.header):
            if key != 'id':
                data[key] = val[i]
        # data['name'] = data['name'] + '12'
        print(id, data)
        # self.currTable.rec_update(id, data)
        # self.refresh_table()

    def filter(self):
        if self.fltCheck.isChecked():
            self.fltLabel1.show()
            self.fltCombo1.show()
            self.fltLabel2.show()
            self.fltCombo2.show()
            self.fltLabel3.show()
            self.fltCombo3.show()
        else:
            self.fltLabel1.hide()
            self.fltCombo1.hide()
            self.fltLabel2.hide()
            self.fltCombo2.hide()
            self.fltLabel3.hide()
            self.fltCombo3.hide()

    def change_table(self):
        self.tableLabel.setText(self.listBox.currentText())

        self.currTable = self.table_list[self.listBox.currentIndex()][1]
        self.currTable.update()
        # self.currTable = self.table_list[self.listWidget.currentRow()][1]
        self.refresh_table()
        self.tableView.selectRow(0)
