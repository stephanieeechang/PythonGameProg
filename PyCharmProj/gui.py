import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox, QComboBox
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Unit Converter')

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Select")
        self.comboBox.addItem("Convert minutes to calories")
        self.comboBox.addItem("Convert calories to minutes")
        self.comboBox.move(40, 30)
        self.comboBox.activated[str].connect(self.styleChoice)

        self.btn1 = QPushButton('Convert', self)
        self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn1.resize(200, 20)
        self.btn1.move(50, 60)
        self.btn1.clicked.connect(self.convert)

        self.text1 = QTextEdit(self)
        self.text1.resize(200, 40)
        self.text1.move(50, 80)

        self.num = QDoubleSpinBox(self)
        self.num.resize(200,30)
        self.num.move(50,130)

        self.setWindowIcon(QIcon('one_punch_icon.png'))

        self.show()

    def convert(self):
        text = str(self.comboBox.currentText())

        if text is "Convert minutes to calories":
            if self.text1.toPlainText() is not "":
                minute = int(self.text1.toPlainText())
                self.num.setValue(minute * 1.5)
        else:
            if self.text1.toPlainText() is not "":
                calories = int(self.text1.toPlainText())
                self.num.setValue(calories / 1.5)

    def styleChoice(self, text):
        if text == "Convert minutes to calories":
            self.text1.setPlaceholderText("Enter minutes spent thinking hard")

            self.num.setMinimum(0)
            self.num.setSuffix(" calories")

        else:
            self.text1.setPlaceholderText("Enter calories wanted to burn")

            self.num.setMinimum(0)
            self.num.setSuffix(" minutes")

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
