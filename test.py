from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtCore import QModelIndex, Qt
import numpy as np
from PyQt5.QtWidgets import QAbstractItemView

from classes.db_session import connectdb
from classes.db_classes import Users, Courses, Groups


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    con = connectdb('db\\database_J.db')
    u = Users(con)
    view = QtWidgets.QTableView()
    view.setModel(u.model())
    view.resizeColumnsToContents()
    view.setSelectionBehavior(QAbstractItemView.SelectRows)

    view.show()
    sys.exit(app.exec())