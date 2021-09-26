import sys
from PyQt5.QtWidgets import QApplication
from classes.db_session import connectdb
from classes.db_classes import Logger
from widgets.w_syslogin import LoginDialog
from widgets.w_mainwindow import MWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    con = connectdb('db\\database_J.db')
    log = Logger(con)
    log.out(('', '', '', '', 'Старт программы'))
    login_user = LoginDialog(con)
    login_user.show()
    app.exec()
    if login_user.passwd_ok:
        log.out((login_user.loggedUser['id'], login_user.loggedUser['name'], '', '', 'Успешный вход'))
        wnd = MWindow(con)
        wnd.showMaximized()
        sys.exit(app.exec())

