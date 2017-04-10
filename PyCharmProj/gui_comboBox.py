import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox

class ComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Combo Box')

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("LASAGNA")
        self.comboBox.addItem("CHICKEN MARSALA")
        self.comboBox.addItem("ANGEL HAIR POMODORO")
        self.comboBox.move(50, 50)

        self.show()


app = QApplication(sys.argv)
cb = ComboBox()
sys.exit(app.exec_())
