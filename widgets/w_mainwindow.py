from PyQt5.QtWidgets import QLabel, QMainWindow, QAbstractItemView, QMessageBox, QLineEdit, \
    QComboBox, QDialogButtonBox, QHBoxLayout
from PyQt5 import QtGui     # , uic
from PyQt5.QtCore import Qt
from classes.cl_users import Users
from classes.db_classes import Privileges, Roles, Places, Courses, GroupTable, Groups
from classes.bb_converts import *
from widgets.MainWindow import Ui_MainWindow
from widgets.w_tab3form import tab3FormWindow


class MWindow(QMainWindow, Ui_MainWindow):  # Главное окно приложения
    def __init__(self, con):
        super(MWindow, self).__init__()
        self.setupUi(self)
        # uic.loadUi('widgets\\MainWindow.ui', self)
        self.initUi(con)

    def initUi(self, con):
        self.setWindowTitle('IT-куб. Белая Холуница. Журналы. v.0.9')
        self.con = con
        self.id = None
        self.currTable = None
        self.edit_widgets = []
        self.table_list = {
            0: ('Привилегии доступа', Privileges(self.con)),
            1: ('Роли пользователей', Roles(self.con)),
            2: ('Места работы/учёбы', Places(self.con)),
            3: ('Учебные программы', Courses(self.con)),
            4: ('Учебные группы', Groups(self.con))
#            5: ('Списки учебных групп', GroupTable(self.con))
        }
        self.listBox.addItems([val[0] for val in self.table_list.values()])
        self.listBox.currentIndexChanged.connect(self.tab1_change_table)
        self.listBox.setCurrentIndex(3)

        self.myLayout = QHBoxLayout(self)
        self.tab3.setLayout(self.myLayout)
        self.myLayout.addWidget(tab3FormWindow(con))
        # self.wtab3 = tab3FormWindow(con)

        # self.MainTab.setCurrentIndex(0)
        self.tableView.doubleClicked.connect(self.edit_Button.click)  # ------------------
        self.MainTab.currentChanged.connect(self.main_prepare_tab)
        self.buttonEditFrame.button(QDialogButtonBox.Save).setText('Сохранить')
        self.buttonEditFrame.button(QDialogButtonBox.No).setText('Отмена')
        self.fltCheck.stateChanged.connect(self.tab1_filter)
        self.add_Button.clicked.connect(self.tab1_clicked_buttons)
        self.edit_Button.clicked.connect(self.tab1_clicked_buttons)
        self.del_Button.clicked.connect(self.tab1_clicked_buttons)
        self.commit_Button.clicked.connect(self.tab1_clicked_buttons)
        self.rollback_Button.clicked.connect(self.tab1_clicked_buttons)
        self.buttonEditFrame.rejected.connect(self.tab1_deactivateEditFrame)
        self.buttonEditFrame.accepted.connect(self.tab1_save_edit_frame)
        self.MainTab.tabBarClicked.connect(self.check_for_commit)
        self.tab2_buttonBox.button(QDialogButtonBox.Save).setText('Сохранить')
        self.tab2_buttonBox.button(QDialogButtonBox.Cancel).setText('Отмена')
        self.currTable.need_to_save.connect(self.tab2_refresh_form)
        self.tableView_Users.doubleClicked.connect(self.tab2_edit_form)
        self.tab2_del.clicked.connect(self.tab2_clicked_buttons)
        self.tab2_add.clicked.connect(self.tab2_clicked_buttons)
        self.tab2_edit.clicked.connect(self.tab2_clicked_buttons)
        self.tab2_commit.clicked.connect(self.tab2_clicked_buttons)
        self.tab2_rollback.clicked.connect(self.tab2_clicked_buttons)
        self.tab2_buttonBox.rejected.connect(self.tab2_deactivateEditFrame)
        self.tab2_buttonBox.accepted.connect(self.tab2_save_edit_frame)


        self.MainTab.setCurrentIndex(1)
        self.tab2_activate()

    def main_prepare_tab(self):
        """ Переключение окон главного окна """
        if self.tab1.isVisible():
            self.tab1_activate()
        elif self.tab2.isVisible():
            self.tab2_activate()
        elif self.tab3.isVisible():
            print('tab3')
            # self.tab3.show()
        elif self.tab4.isVisible():
            print('tab4')
        elif self.tab5.isVisible():
            print('tab5')
        elif self.tab6.isVisible():
            print('tab6')

    def create_edit_widgets(self, curLayout):
        """ Создание полей редактирования записи """
        self.current_data = self.currTable.get_record(self.id)
        self.delete_edit_form(curLayout)
        for i, val in enumerate(self.current_data):
            self.edit_widgets.append(QLabel(val[1], self))
            curLayout.addWidget(self.edit_widgets[-1], i + 2, 0)
            if val[0][:2] == 'id':
                self.edit_widgets.append(QComboBox(self))
                self.edit_widgets[-1].setFocusPolicy(Qt.StrongFocus)
                curLayout.addWidget(self.edit_widgets[-1], i + 2, 1)
                sql = f"""select id || " : " || name || " : " ||  comment from {val[0][2:]}"""
                # sql = f"select name from {val[0][2:]}"
                cur = self.con.cursor()
                spis = cur.execute(sql).fetchall()
                self.edit_widgets[-1].addItems([val[:][0] for val in spis])
                for i in range(self.edit_widgets[-1].count()):
                    fnd = self.edit_widgets[-1].itemText(i)
                    id = fnd[:fnd.find(':') - 1]
                    if id == str(val[2]):
                        self.edit_widgets[-1].setCurrentIndex(i)
            else:
                if val[0] == 'birthday':
                    val[2] = date_us_ru(val[2])
                self.edit_widgets.append(QLineEdit(str(val[2]), self))
                curLayout.addWidget(self.edit_widgets[-1], i + 2, 1)
            self.edit_widgets[1].setFocus()

    def update_edit_frame(self):
        """ Сохраняем результаты редактирования. либо создание новой записи """
        arg = {}
        for i, widg in enumerate(self.edit_widgets[1::2]):
            if type(widg) == QLineEdit:
                if self.current_data[i][0] == 'birthday':
                    arg[self.current_data[i][0]] = date_ru_us(widg.text())
                else:
                    arg[self.current_data[i][0]] = widg.text().replace(':', '-')
            elif type(widg) == QComboBox:
                fnd = widg.currentText()
                id = fnd[:fnd.find(':') - 1]
                arg[self.current_data[i][0]] = str(id)
            else:
                print('Ошибочный тип в редакторе!')
        for widg in self.edit_widgets:
            widg.deleteLater()
        self.edit_widgets.clear()
        if self.id == 0:
            self.currTable.rec_append(arg)
        else:
            self.currTable.rec_update(self.id, arg)

    def delete_edit_form(self, curLayout):
        """ Удаляем поля редактирования """
        for widg in self.edit_widgets:
            curLayout.removeWidget(widg)
            widg.deleteLater()
        self.edit_widgets.clear()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """ Проверка на сохранение данных при выходе из программы """
        self.check_for_commit()
        return QMainWindow.closeEvent(self, a0)

    def check_for_commit(self):
        """ Диалог для COMMIT - ROLLBACK изменений """
        if self.currTable.con.in_transaction:
            buttonReply = QMessageBox.question(self, 'Редактор', "Остались несохранённые изменения, сохранить?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.currTable.commit()
            else:
                self.currTable.rollback()

    def tab1_clicked_buttons(self):
        """ Обработка нажатий правого поля кнопок на ТАБ 1"""
        obj_name = self.sender().objectName()
        if obj_name == 'del_Button':
            self.currTable.rec_delete(self.currTable.data[self.tableView.currentIndex().row()][0])
            self.tab1_refresh_table()
            return
        elif obj_name == 'commit_Button':
            self.currTable.commit()
            self.tab1_refresh_table()
            return
        elif obj_name == 'rollback_Button':
            self.currTable.rollback()
            self.tab1_refresh_table()
            return
        elif obj_name == 'edit_Button':
            self.id = self.currTable.data[self.tableView.currentIndex().row()][0]
        elif obj_name == 'add_Button':
            self.id = 0
            self.current_data = []
        self.create_edit_widgets(self.gridLayout)
        self.editFrame.show()
        for button in self.buttonMainGroup.buttons():
            button.setDisabled(True)
        self.listBox.setDisabled(True)

    def tab1_refresh_table(self):
        """ Смена текушей таблицы. Обновление формы """
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

    def tab1_filter(self):
        """ Работа с фильтром данных """
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

    def tab1_change_table(self):
        """ Переключаем текущую таблицу """
        self.tableLabel.setText(self.listBox.currentText())
        self.currTable = self.table_list[self.listBox.currentIndex()][1]
        self.currTable.update()
        self.tab1_refresh_table()
        self.tableView.selectRow(0)

    def tab1_deactivateEditFrame(self):
        self.delete_edit_form(self.gridLayout)
        self.editFrame.hide()
        for button in self.buttonMainGroup.buttons():
            button.setDisabled(False)
        self.listBox.setDisabled(False)
        self.tab1_refresh_table()

    def tab1_save_edit_frame(self):
        self.update_edit_frame()
        self.tab1_deactivateEditFrame()

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
        self.create_edit_widgets(self.gridLayout_2)
        self.tableView_Users.setDisabled(True)
        self.frame_users.show()
        # self.editFrame.show()
        for button in self.tab2_buttonGroup.buttons():
            button.setDisabled(True)

    def tab2_deactivateEditFrame(self):
        self.delete_edit_form(self.gridLayout_2)
        self.frame_users.hide()
        for button in self.tab2_buttonGroup.buttons():
            button.setDisabled(False)
        self.tableView_Users.setDisabled(False)
        self.tab2_refresh_form()

    def tab2_save_edit_frame(self):
        self.update_edit_frame()
        self.tab2_deactivateEditFrame()

    def tab1_activate(self):
        self.delete_edit_form(self.gridLayout)
        self.tab1_change_table()
        self.editFrame.hide()
        self.fltCheck.setChecked(True)
        self.fltCheck.setChecked(False)
        # Фильтр списка

    def tab2_activate(self):
        self.delete_edit_form(self.gridLayout_2)
        self.frame_users.hide()
        self.currTable = Users(self.con, editable=True)
        self.tableView_Users.setModel(self.currTable.model())
        self.tableView_Users.resizeColumnsToContents()
        self.tableView_Users.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab2_deactivateEditFrame()

