import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication
from PyQt5.QtGui import QFont


MORSE_ENG = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
             'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
             'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
             'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
             'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
             'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
             'y': '-.--', 'z': '--..'}


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Азбука Морзе 2")
        # self.setGeometry()
        self.font = QFont('Times', 13, QFont.Normal)

        self.in1 = QLineEdit(self)
        self.in1.resize(400, 20)
        self.in1.setFont(self.font)
        self.in1.move(10, 60)

        keys_btn = list(MORSE_ENG.keys())
        self.btns = []
        for i in range(20):
            self.btns.append(QPushButton(keys_btn[i], self))
            self.btns[i].resize(25, 25)
            self.btns[i].move(20 + i * 25, 5)
            self.btns[i].setFont(self.font)
            self.btns[i].clicked.connect(self.click)
        for i in range(6):
            self.btns.append(QPushButton(keys_btn[i + 20], self))
            self.btns[i + 20].resize(25, 25)
            self.btns[i + 20].move(20 + i * 25, 30)
            self.btns[i + 20].setFont(self.font)
            self.btns[i + 20].clicked.connect(self.click)

        self.btns.append(QPushButton("clear", self))
        self.btns[-1].resize(40, 40)
        self.btns[-1].move(480, 80)
        self.btns[-1].clicked.connect(self.click)

        self.adjustSize()
        self.show()

    def click(self):
        vbtn = self.sender().text()
        if vbtn == "clear":
            self.in1.setText("")
        else:
            self.in1.setText(f"{self.in1.text()} {MORSE_ENG[vbtn]}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    sys.exit(app.exec())
