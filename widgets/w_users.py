import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QTableWidget



class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.centralWidget = QTableWidget(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    sys.exit(app.exec())
