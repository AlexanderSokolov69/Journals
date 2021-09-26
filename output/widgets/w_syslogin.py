import sqlite3
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QTableWidget
from classes.cl_password import Password
from classes.cl_users import Users
from .loginDlg import Ui_Dialog


class LoginDialog(QWidget, Ui_Dialog):
    def __init__(self, con):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.initUI(con)

    def initUI(self, con):
        self.user = Users(con)
        self.passwd2.hide()
        self.passwd_ok = False
        self.loggedUser = None
        self.setFixedSize(480, 210)

        self.show()

    def accept(self):
        self.loggedUser = self.user.get_user_login(self.login.text())
        if self.loggedUser:
            self.label_err.setText(str(self.loggedUser['name']))
            psw = Password('')
            if not self.loggedUser['passwd']:
                if self.passwd.text() != self.passwd2.text() or not self.passwd2.text():
                    self.passwd2.show()
                    self.label_err.setText(f"{str(self.loggedUser['name'])} введите новый пароль 2 раза..")
                else:
                    self.passwd2.hide()
                    psw = Password(self.passwd2.text())
                    self.user.set_user_password(self.loggedUser['id'], psw.get_storage())
                    self.user.get_user_login(self.login.text())
            else:
                psw.set_storage(self.loggedUser['passwd'])
                if psw.check_passwd(self.passwd.text().strip()):
                    self.label_err.setText('Пароль верный!')
                    self.passwd_ok = True
                    self.close()
                else:
                    self.label_err.setText('Ошибка в имени или пароле!')
        else:
            self.label_err.setText('Ошибка в имени или пароле!')

    def reject(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    con = sqlite3.connect('..\\db\\database_J.db')
    wnd = LoginDialog(con)
    sys.exit(app.exec())
