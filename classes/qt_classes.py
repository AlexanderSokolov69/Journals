from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt



class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, head, data=[[]]):
        super(MyTableModel, self).__init__()
        self.data = data
        self.head = head

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
            self.data.sort(key=lambda i: i[section])
            self.endResetModel()


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
        else:
            ret = ' '
        if role == QtCore.Qt.DisplayRole:
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
