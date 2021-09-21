from PyQt5 import QtCore
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

    def columnCount(self, parent=None):
        return len(self.data[0])

    def rowCount(self, parent=None):
        return len(self.data)

    def data(self, index, role):
        row = index.row()
        col = index.column()
        ret = self.data[row][col]
        if role == QtCore.Qt.DisplayRole:
            if ret is None:
                return ""
            else:
                return str(ret)
        # if role == Qt.TextAlignmentRole:
        #     if isinstance(ret, int) or isinstance(ret, float):
        #         # Align right, vertical middle.
        #         return Qt.AlignVCenter + Qt.AlignRight
        # if role == Qt.BackgroundRole and index.column() == 2:
        #     # See below for the data structure.
        #     return QtGui.QColor('blue')
