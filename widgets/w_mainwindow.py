from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QAbstractItemView

from classes.cl_users import Users
from widgets.MainWindow import Ui_MainWindow


class MWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, con):
        super(MWindow, self).__init__()
        self.setupUi(self)
        self.initUi(con)

    def initUi(self, con):
        self.con = con
        self.table_list = {
            0: ('Роли пользователей', 'Roles()'),
            1: ('Права доступа', 'Priv()'),
            2: ('Места работы/учёбы', 'Places()'),
            3: ('Учебные программы', 'Cources()'),
            4: ('Учебные группы', 'Groups()'),
            5: ('Списки учебных групп', 'GroupTable()')
        }
        self.tableView.resizeColumnsToContents()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.listWidget.addItems([val[0] for val in self.table_list.values()])
        self.listWidget.adjustSize()
        self.listWidget.itemSelectionChanged.connect(self.change_table)
        self.listWidget.setCurrentItem(self.listWidget.item(0))
        self.currTable = None


    def change_table(self):
        self.tableLabel.setText(self.listWidget.currentItem().text())
        self.currTable = Users(self.con)
        self.tableView.setModel(self.currTable.model())
        self.tableView.selectRow(0)
