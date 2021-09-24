import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class TableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(TableModel, self).__init__(parent)

        self.tasks = [[['%d - %d' % (i, j), False] for j in range(7)] for i in range(10)]  # +++

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.tasks)

    def columnCount(self, parent=None, *args, **kwargs):
        return 7

    def headerData(self, section, orientation, role=None):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return ["Задача", "Дата начала", "Дата конца",
                        "Отдел", "Кол-во человек", "Трудоёмкость",
                        "Выполнение"][section]

    def data(self, index, role):
        if index.isValid():
            data, changed = self.tasks[index.row()][index.column()]

            if role in [Qt.DisplayRole, Qt.EditRole]:
                return data

    def setData(self, index, value, role):  # !!!
        if role == Qt.EditRole:
            self.tasks[index.row()][index.column()] = [value, True]
            return True
        return False

    def flags(self, index):  # !!!
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = TableModel()
        self.table = QTableView()
        self.table.verticalHeader().hide()
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setModel(self.model)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        grid = QGridLayout(centralWidget)
        grid.addWidget(self.table, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(750, 300)
    mw.show()
    sys.exit(app.exec_())
    