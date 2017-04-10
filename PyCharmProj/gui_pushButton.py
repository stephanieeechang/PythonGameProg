import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class PushButton(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Click a button')

        self.btn1 = QPushButton('Button A', self)
        self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn1.resize(200, 40)
        self.btn1.move(50, 60)
        self.btn1.clicked.connect(self.pushA)

        self.btn2 = QPushButton('Button B', self)
        self.btn2.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn2.resize(200, 40)
        self.btn2.move(50, 100)
        self.btn2.clicked.connect(self.pushB)

        self.show()

    def pushA(self):
        self.setWindowTitle('Button A clicked')

    def pushB(self):
        self.setWindowTitle('Button B clicked')


app = QApplication(sys.argv)
pb = PushButton()
sys.exit(app.exec_())

