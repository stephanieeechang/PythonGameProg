import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class Label(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle('gui demo')

        self.label1 = QLabel(self)
        self.label1.setText('Heman generator!')
        self.label1.move(390, 40)

        self.label2 = QLabel(self)
        self.label2.setToolTip('https://www.youtube.com/watch?v=ZZ5LpwO-An4')
        self.label2.setText('''<a href='https://www.youtube.com/watch?v=ZZ5LpwO-An4'>What's going on?</a>''')
        self.label2.move(390, 90)
        self.label2.setOpenExternalLinks(True)

        self.label3 = QLabel(self)
        self.label3.move(80, 130)
        self.label3.setPixmap(QPixmap("heman.jpg"))

        self.show()

app = QApplication(sys.argv)
lb = Label()
lb.show()
sys.exit(app.exec_())
