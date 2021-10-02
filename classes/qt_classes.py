from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QTableView

from classes.bb_converts import *
import datetime


class MyTableModel(QtCore.QAbstractTableModel):
    need_save = pyqtSignal()
    need_edit = pyqtSignal()
    sort_col = 0

    def __init__(self, head, data=[[]], editable=False, date_col=8):
        super(MyTableModel, self).__init__()
        self.data = data
        self.head = head
        self.editable = editable
        self.date_col = date_col
        self.current_index = (-1, -1)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.head[section]
            else:
                return ''
        if role == Qt.BackgroundColorRole: # BackgroundRole:
            # See below for the data structure.
            return QtGui.QColor('#c0f0f0')
        if role == Qt.InitialSortOrderRole:
            self.beginResetModel()
            if self.sort_col == section:
                self.data.sort(key=lambda i: i[section], reverse=True)
                self.sort_col = -1
            else:
                self.data.sort(key=lambda i: i[section])
                self.sort_col = section
            self.endResetModel()
            return
        # if role not in [4]:
        #     print(section, orientation, role)

    def columnCount(self, parent=None):
            return len(self.head)

    def rowCount(self, parent=None):
            return len(self.data)

    def data(self, index, role):
        ret = None
        if len(self.data[0]) > 0:
            row = index.row()
            col = index.column()
            ret = self.data[row][col]
            if col == self.date_col:
                ret = date_us_ru(ret)
        else:
            ret = ' '
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if ret is None:
                return ""
            else:
                return str(ret)
        if role == Qt.TextAlignmentRole:
            if isinstance(ret, int) or isinstance(ret, float):
                # Align right, vertical middle.
                return Qt.AlignVCenter + Qt.AlignRight
        if role == Qt.BackgroundRole and index.row() % 2:
            # See below for the data structure.
            return QtGui.QColor('#f0fcfc')

    def setData(self, index, value, role):  # !!!
        if role == Qt.EditRole:
            if index.column() > 0:
                if index.column() == self.date_col:
                    value = date_ru_us(value)
                self.data[index.row()][index.column()] = str(value).strip(' \n.').replace(':', '-')
                self.current_index = (index.row(), index.column())
                self.need_save.emit()
                return True
        return False

    def flags(self, index):  # !!!
        if self.editable and index.column() in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        else:
            # if index.column() == 0:
            #     self.need_edit.emit()
            # self.current_index = (0, 0)
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
