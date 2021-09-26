from PyQt5.QtWidgets import QLabel, QMainWindow, QAbstractItemView, QMessageBox, QLineEdit, QComboBox, QDialogButtonBox, \
    QTableView
from PyQt5 import QtGui, uic

from classes.cl_users import Users
from classes.db_classes import Privileges, Roles, Places, Courses, GroupTable, Groups
from widgets.MainWindow import Ui_MainWindow


class MWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, con):
        super(MWindow, self).__init__()
        uic.loadUi('widgets\\MainWindow.ui', self)
        # self.setupUi(self)
        self.initUi(con)

    def initUi(self, con):
        self.setWindowTitle('IT-куб. Белая Холуница. Журналы. v.0.9')
        self.con = con
        self.id = None
        self.currTable = None
        self.editFrame.hide()
        self.edit_widgets = []
        self.table_list = {
            0: ('Привилегии доступа', Privileges(self.con)),
            1: ('Роли пользователей', Roles(self.con)),
            2: ('Места работы/учёбы', Places(self.con)),
            3: ('Учебные программы', Courses(self.con)),
            4: ('Учебные группы', Groups(self.con)),
            5: ('Списки учебных групп', GroupTable(self.con))
        }

        self.listBox.addItems([val[0] for val in self.table_list.values()])
        self.listBox.currentIndexChanged.connect(self.change_table)
        self.listBox.setCurrentIndex(3)

        self.buttonEditFrame.button(QDialogButtonBox.Save).setText('Сохранить')
        self.buttonEditFrame.button(QDialogButtonBox.No).setText('Отмена')

        # Фильтр списка
        self.fltCheck.stateChanged.connect(self.filter)
        self.fltCheck.setChecked(True)
        self.fltCheck.setChecked(False)

        self.add_Button.clicked.connect(self.clicked_buttons)
        self.edit_Button.clicked.connect(self.clicked_buttons)
        self.del_Button.clicked.connect(self.clicked_buttons)
        self.commit_Button.clicked.connect(self.clicked_buttons)
        self.rollback_Button.clicked.connect(self.clicked_buttons)

        self.buttonEditFrame.rejected.connect(self.deactivateEditFrame)
        self.buttonEditFrame.accepted.connect(self.save_edit_frame)

        self.tableView.doubleClicked.connect(self.edit_Button.click)  # ------------------

        self.MainTab.tabBarClicked.connect(self.check_for_save)
        self.MainTab.currentChanged.connect(self.prepare_tab)

        self.MainTab.setCurrentIndex(0)


    def check_for_save(self):
        if self.currTable.con.in_transaction:
            buttonReply = QMessageBox.question(self, 'Редактор', "Остались несохранённые изменения, сохранить?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.currTable.commit()
            else:
                self.currTable.rollback()

    def signal_closeEvent(a0):
        return super().closeEvent(a0)

    def clicked_buttons(self):
        obj_name = self.sender().objectName()
        if obj_name == 'del_Button':
            self.currTable.rec_delete(self.currTable.data[self.tableView.currentIndex().row()][0])
            self.refresh_table()
            return
        elif obj_name == 'commit_Button':
            self.currTable.commit()
            self.refresh_table()
            return
        elif obj_name == 'rollback_Button':
            self.currTable.rollback()
            self.refresh_table()
            return
        elif obj_name == 'edit_Button':
            self.id = self.currTable.data[self.tableView.currentIndex().row()][0]
        elif obj_name == 'add_Button':
            self.id = 0
            self.current_data = []
        self.create_edit_frame()
        self.editFrame.show()
        for button in self.buttonMainGroup.buttons():
            button.setDisabled(True)
        self.listBox.setDisabled(True)

    def refresh_table(self):
        self.currTable.update()
        self.tableLabel.setText(f"{self.listBox.currentText()}   ({len(self.currTable.data)})")
        self.tableView.setModel(self.currTable.model())
        self.tableView.resizeColumnsToContents()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        if self.currTable.con.in_transaction:
            self.transLabel.setText('')
            self.commit_Button.setFlat(False)
            self.rollback_Button.setFlat(False)
            self.commit_Button.setDisabled(False)
            self.rollback_Button.setDisabled(False)
        else:
            self.transLabel.setText('')
            self.commit_Button.setFlat(True)
            self.rollback_Button.setFlat(True)
            self.commit_Button.setDisabled(True)
            self.rollback_Button.setDisabled(True)
        if len(self.currTable.data[0]) == 0:
            self.del_Button.setDisabled(True)
            self.edit_Button.setDisabled(True)
        else:
            self.del_Button.setDisabled(False)
            self.edit_Button.setDisabled(False)

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
#        self.currTable.need_to_save.connect(self.sig)
        self.currTable.update()
        self.refresh_table()
        self.tableView.selectRow(0)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.check_for_save()
        return QMainWindow.closeEvent(self, a0)

    def create_edit_frame(self):
        self.current_data = self.currTable.get_record(self.id)
        for i, val in enumerate(self.current_data):
            self.edit_widgets.append(QLabel(val[1], self))
            self.gridLayout.addWidget(self.edit_widgets[-1], i + 2, 0)
            if val[0][:2] == 'id':
                self.edit_widgets.append(QComboBox(self))
                self.gridLayout.addWidget(self.edit_widgets[-1], i + 2, 1)
                sql = f"select name from {val[0][2:]}"
                cur = self.con.cursor()
                spis = cur.execute(sql).fetchall()
                self.edit_widgets[-1].addItems([val[:][0] for val in spis])
            else:
                self.edit_widgets.append(QLineEdit(str(val[2]), self))
                self.gridLayout.addWidget(self.edit_widgets[-1], i + 2, 1)

    def deactivateEditFrame(self):
        for widg in self.edit_widgets:
            self.gridLayout.removeWidget(widg)
            widg.deleteLater()
        self.edit_widgets.clear()
        self.editFrame.hide()
        for button in self.buttonMainGroup.buttons():
            button.setDisabled(False)
        self.listBox.setDisabled(False)
        self.refresh_table()

    def save_edit_frame(self):
        arg = {}
        for i, widg in enumerate(self.edit_widgets[1::2]):
            if type(widg) == QLineEdit:
                arg[self.current_data[i][0]] = widg.text()
            elif type(widg) == QComboBox:
                base = self.current_data[i][0][2:]
                fnd = widg.currentText()
                sql = f"select id from {base} where name = '{fnd}'"
                cur = self.con.cursor()
                id = cur.execute(sql).fetchone()

                arg[self.current_data[i][0]] = str(id[0])
            else:
                print('Ошибочный тип в редакторе!')

        if self.id == 0:
            self.currTable.rec_append(arg)
        else:
            self.currTable.rec_update(self.id, arg)

        self.deactivateEditFrame()

    def prepare_tab(self):
        if self.tab1.isVisible():
            self.change_table()

        elif self.tab2.isVisible():
            self.frame_users.hide()
            self.currTable = Users(self.con)
            self.currTable.update()
            self.tableView_Users.setModel(self.currTable.model())
            self.tableView_Users.resizeColumnsToContents()
            self.tableView_Users.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.currTable.need_to_save.connect(self.tab2_refresh_form)
            self.tableView_Users.doubleClicked.connect(self.tab2_edit_form)
            self.tab2_del.clicked.connect(self.tab2_clicked_buttons)
            self.tab2_add.clicked.connect(self.tab2_clicked_buttons)
            self.tab2_edit.clicked.connect(self.tab2_clicked_buttons)
            self.tab2_commit.clicked.connect(self.tab2_clicked_buttons)
            self.tab2_rollback.clicked.connect(self.tab2_clicked_buttons)
            # self.tab2_buttonGroup.buttonClicked.connect(self.tab2_clicked_buttons)
            self.tab2_buttonBox.rejected.connect(self.tab2_deactivateEditFrame)
            self.tab2_buttonBox.accepted.connect(self.tab2_save_edit_frame)
            self.tab2_refresh_form()

        elif self.tab3.isVisible():
            print('tab3')
        elif self.tab4.isVisible():
            print('tab4')
        elif self.tab5.isVisible():
            print('tab5')

    def tab2_refresh_form(self):
        if self.currTable.con.in_transaction:
            self.tab2_commit.setFlat(False)
            self.tab2_rollback.setFlat(False)
            self.tab2_commit.setDisabled(False)
            self.tab2_rollback.setDisabled(False)
        else:
            self.tab2_commit.setFlat(True)
            self.tab2_rollback.setFlat(True)
            self.tab2_commit.setDisabled(True)
            self.tab2_rollback.setDisabled(True)
        if len(self.currTable.data[0]) == 0:
            self.tab2_del.setDisabled(True)
            self.tab2_edit.setDisabled(True)
        else:
            self.tab2_del.setDisabled(False)
            self.tab2_edit.setDisabled(False)
        self.currTable.update()
        self.tableView_Users.setModel(self.currTable.model())
        self.tableView_Users.resizeColumnsToContents()
        self.tableView_Users.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lcdNumber_Users.display(len(self.currTable.data))

    def tab2_edit_form(self):
        if self.tableView_Users.currentIndex().column() not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.tab2_edit.click()

    def tab2_clicked_buttons(self):
        obj_name = self.sender().objectName()
        #self.tab2_buttonGroup.buttonClicked
        if obj_name == 'tab2_del':
            self.currTable.rec_delete(self.currTable.data[self.tableView_Users.currentIndex().row()][0])
            self.tab2_refresh_form()
            return
        elif obj_name == 'tab2_commit':
            self.currTable.commit()
            self.tab2_refresh_form()
            return
        elif obj_name == 'tab2_rollback':
            self.currTable.rollback()
            self.tab2_refresh_form()
            return
        elif obj_name == 'tab2_edit':
            self.id = self.currTable.data[self.tableView_Users.currentIndex().row()][0]
        elif obj_name == 'tab2_add':
            self.id = 0
            self.current_data = []
        self.tab2_create_edit_frame()
        # self.editFrame.show()
        for button in self.tab2_buttonGroup.buttons():
            button.setDisabled(True)

    def tab2_create_edit_frame(self):
        self.current_data = self.currTable.get_record(self.id)
        self.edit_widgets.clear()
        for i, val in enumerate(self.current_data):
            self.edit_widgets.append(QLabel(val[1], self))
            self.gridLayout_2.addWidget(self.edit_widgets[-1], i + 2, 0)
            if val[0][:2] == 'id':
                self.edit_widgets.append(QComboBox(self))
                self.gridLayout_2.addWidget(self.edit_widgets[-1], i + 2, 1)
                sql = f"select name from {val[0][2:]}"
                cur = self.con.cursor()
                spis = cur.execute(sql).fetchall()
                self.edit_widgets[-1].addItems([val[:][0] for val in spis])
            else:
                self.edit_widgets.append(QLineEdit(str(val[2]), self))
                self.gridLayout_2.addWidget(self.edit_widgets[-1], i + 2, 1)
        self.tableView_Users.setDisabled(True)
        self.frame_users.show()

    def tab2_deactivateEditFrame(self):
        for widg in self.edit_widgets:
            self.gridLayout_2.removeWidget(widg)
            widg.deleteLater()
        self.edit_widgets.clear()
        self.frame_users.hide()
        for button in self.tab2_buttonGroup.buttons():
            button.setDisabled(False)
        self.tableView_Users.setDisabled(False)
        self.tab2_refresh_form()

    def tab2_save_edit_frame(self):
        arg = {}
        for i, widg in enumerate(self.edit_widgets[1::2]):
            if type(widg) == QLineEdit:
                arg[self.current_data[i][0]] = widg.text()
            elif type(widg) == QComboBox:
                base = self.current_data[i][0][2:]
                fnd = widg.currentText()
                sql = f"select id from {base} where name = '{fnd}'"
                cur = self.con.cursor()
                id = cur.execute(sql).fetchone()

                arg[self.current_data[i][0]] = str(id[0])
            else:
                print('Ошибочный тип в редакторе!')

        if self.id == 0:
            self.currTable.rec_append(arg)
        else:
            self.currTable.rec_update(self.id, arg)

        self.tab2_deactivateEditFrame()
