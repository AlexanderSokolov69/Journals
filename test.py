import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QAbstractItemView

from classes.db_session import connectdb
from classes.db_classes import Users, Courses, Groups, Password
from widgets.w_syslogin import LoginDialog

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    con = connectdb('db\\database_J.db')

    login_user = LoginDialog(con)
    wnd = Window()
#     u = Groups(con)
#     view = QtWidgets.QTableView()
#     view.setModel(u.model())
#     view.resizeColumnsToContents()
#     view.setSelectionBehavior(QAbstractItemView.SelectRows)
#     us = Users(con)
#     res = us.get_user_login('falcon')
#     psw = Password('1234')
# #    us.set_user_password(res['id'], psw.get_storage())
# #    print(res['passwd'])
# #    print(type(res['passwd']))
#     psw.set_storage(res['passwd'])

    # hash = res['passwd']
    # hash2 = psw.get_storage()
    # print(hash, hash2, sep='\n')
    # print(psw.check_passwd('1234'))
    # view.show()
    # sys.exit(app.exec())
    app.exec()
    if login_user.passwd_ok:
        print(login_user.loggedUser['fio'])
        print(login_user.loggedUser['phone'])

        wnd.show()
        app.exec()
