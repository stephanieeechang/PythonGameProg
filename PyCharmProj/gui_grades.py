import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QIntValidator

class Grades(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Grade Converter')

        self.text1 = QLineEdit(self)
        self.text1.resize(200, 40)
        self.text1.move(50, 80)
        self.text1.textChanged.connect(self.letterGrade)
        self.text1.setPlaceholderText("Enter grade 0-100")
        self.text1.setValidator(QIntValidator(0, 100, self))

        self.text2 = QLineEdit(self)
        self.text2.resize(200, 40)
        self.text2.move(50, 130)

        self.show()

    def letterGrade(self):
        text = int(self.text1.text())
        letters = {'A+':range(97, 101),'A':range(93, 97),'A-':range(90,93),'B+':range(87,90),
                   'B':range(83, 87), 'B-':range(80, 83),'C+':range(77, 80), 'C':range(77, 73),
                   'C-':range(70, 73), 'D+':range(67, 70), 'D':range(63, 67), 'D-':range(60, 63),
                   'F':range(0, 60)}
        if self.text1.text() is not "":
            for k, v in letters.items():
                if text in v:
                    self.text2.setText(k)
        else:
            self.text2.setText('Invalid grade!')

app = QApplication(sys.argv)
gr = Grades()
gr.show()
sys.exit(app.exec_())
