'''
use all widgets taught in the program, including QLabel, QCalendarWidget, QCheckBox,
QDockWidget, QTabWidget and QProgressBar
'''

import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QDockWidget, \
    QCheckBox, QCalendarWidget, QLabel, QTextEdit, QTabWidget, QFormLayout, QHBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, QDate

class Thread(QThread):
    set_max = pyqtSignal(int)
    update = pyqtSignal(int)
    def __init__(wait):
        QThread.__init__(wait)

    def __del__(self):
        self.wait()

    def run(self):
        self.update.emit(100)
        for index in range(0):
            self.update.emit(index)
            time.sleep(0.01)


class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()
        # add tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'Word')
        self.addTab(self.tab2, 'School')
        self.addTab(self.tab3, 'Personal')

        self.tab_1()
        self.tab_2()
        self.tab_3()

        self.thread = Thread()
        self.thread.set_max.connect(self.set_max)
        self.thread.update.connect(self.condition1)
        self.thread.update.connect(self.condition2)
        self.thread.update.connect(self.condition3)

        self.setGeometry(440, 130, 350, 400)

    def tab_1(self):
        layout = QFormLayout()
        # add text edit
        self.text1 = QTextEdit(self)
        self.text1.setPlaceholderText('Add to To-Do-List')
        self.text2 = QTextEdit(self)
        self.text2.setPlaceholderText('Add to To-Do-List')
        self.text3 = QTextEdit(self)
        self.text3.setPlaceholderText('Add to To-Do-List')
        self.text4 = QTextEdit(self)
        self.text4.setPlaceholderText('Add to To-Do-List')
        self.text5 = QTextEdit(self)
        self.text5.setPlaceholderText('Add to To-Do-List')
        # add checkbox
        self.check1 = QCheckBox('', self)
        self.check1.stateChanged.connect(self.condition1)
        self.check2 = QCheckBox('', self)
        self.check2.stateChanged.connect(self.condition1)
        self.check3 = QCheckBox('', self)
        self.check3.stateChanged.connect(self.condition1)
        self.check4 = QCheckBox('', self)
        self.check4.stateChanged.connect(self.condition1)
        self.check5 = QCheckBox('', self)
        self.check5.stateChanged.connect(self.condition1)
        # add progress bar
        self.pb1 = QProgressBar(self)

        self.progressHeading = QLabel(self)
        self.progressHeading.setText("Today's progress")
        self.h1 = QHBoxLayout()
        self.h1.addWidget(self.check1)
        self.h1.addWidget(self.text1)
        self.h2 = QHBoxLayout()
        self.h2.addWidget(self.check2)
        self.h2.addWidget(self.text2)
        self.h3 = QHBoxLayout()
        self.h3.addWidget(self.check3)
        self.h3.addWidget(self.text3)
        self.h4 = QHBoxLayout()
        self.h4.addWidget(self.check4)
        self.h4.addWidget(self.text4)
        self.h5 = QHBoxLayout()
        self.h5.addWidget(self.check5)
        self.h5.addWidget(self.text5)

        layout.addRow(self.h1)
        layout.addRow(self.h2)
        layout.addRow(self.h3)
        layout.addRow(self.h4)
        layout.addRow(self.h5)
        layout.addRow(self.progressHeading)
        layout.addWidget(self.pb1)
        self.tab1.setLayout(layout)

    def tab_2(self):
        layout = QFormLayout()
        # add text edit
        self.text1 = QTextEdit(self)
        self.text1.setPlaceholderText('Add to To-Do-List')
        self.text2 = QTextEdit(self)
        self.text2.setPlaceholderText('Add to To-Do-List')
        self.text3 = QTextEdit(self)
        self.text3.setPlaceholderText('Add to To-Do-List')
        self.text4 = QTextEdit(self)
        self.text4.setPlaceholderText('Add to To-Do-List')
        self.text5 = QTextEdit(self)
        self.text5.setPlaceholderText('Add to To-Do-List')
        # add checkbox
        self.check6 = QCheckBox('', self)
        self.check6.stateChanged.connect(self.condition2)
        self.check7 = QCheckBox('', self)
        self.check7.stateChanged.connect(self.condition2)
        self.check8 = QCheckBox('', self)
        self.check8.stateChanged.connect(self.condition2)
        self.check9 = QCheckBox('', self)
        self.check9.stateChanged.connect(self.condition2)
        self.check10 = QCheckBox('', self)
        self.check10.stateChanged.connect(self.condition2)
        # add progress bar
        self.pb2 = QProgressBar(self)

        self.progressHeading = QLabel(self)
        self.progressHeading.setText("Today's progress")
        self.h1 = QHBoxLayout()
        self.h1.addWidget(self.check6)
        self.h1.addWidget(self.text1)
        self.h2 = QHBoxLayout()
        self.h2.addWidget(self.check7)
        self.h2.addWidget(self.text2)
        self.h3 = QHBoxLayout()
        self.h3.addWidget(self.check8)
        self.h3.addWidget(self.text3)
        self.h4 = QHBoxLayout()
        self.h4.addWidget(self.check9)
        self.h4.addWidget(self.text4)
        self.h5 = QHBoxLayout()
        self.h5.addWidget(self.check10)
        self.h5.addWidget(self.text5)

        layout.addRow(self.h1)
        layout.addRow(self.h2)
        layout.addRow(self.h3)
        layout.addRow(self.h4)
        layout.addRow(self.h5)
        layout.addRow(self.progressHeading)
        layout.addWidget(self.pb2)
        self.tab2.setLayout(layout)

    def tab_3(self):
        layout = QFormLayout()
        # add text edit
        self.text1 = QTextEdit(self)
        self.text1.setPlaceholderText('Add to To-Do-List')
        self.text2 = QTextEdit(self)
        self.text2.setPlaceholderText('Add to To-Do-List')
        self.text3 = QTextEdit(self)
        self.text3.setPlaceholderText('Add to To-Do-List')
        self.text4 = QTextEdit(self)
        self.text4.setPlaceholderText('Add to To-Do-List')
        self.text5 = QTextEdit(self)
        self.text5.setPlaceholderText('Add to To-Do-List')
        # add checkbox
        self.check11 = QCheckBox('', self)
        self.check11.stateChanged.connect(self.condition3)
        self.check12 = QCheckBox('', self)
        self.check12.stateChanged.connect(self.condition3)
        self.check13 = QCheckBox('', self)
        self.check13.stateChanged.connect(self.condition3)
        self.check14 = QCheckBox('', self)
        self.check14.stateChanged.connect(self.condition3)
        self.check15 = QCheckBox('', self)
        self.check15.stateChanged.connect(self.condition3)
        # add progress bar
        self.pb3 = QProgressBar(self)

        self.progressHeading = QLabel(self)
        self.progressHeading.setText("Today's progress")
        self.h1 = QHBoxLayout()
        self.h1.addWidget(self.check11)
        self.h1.addWidget(self.text1)
        self.h2 = QHBoxLayout()
        self.h2.addWidget(self.check12)
        self.h2.addWidget(self.text2)
        self.h3 = QHBoxLayout()
        self.h3.addWidget(self.check13)
        self.h3.addWidget(self.text3)
        self.h4 = QHBoxLayout()
        self.h4.addWidget(self.check14)
        self.h4.addWidget(self.text4)
        self.h5 = QHBoxLayout()
        self.h5.addWidget(self.check15)
        self.h5.addWidget(self.text5)

        layout.addRow(self.h1)
        layout.addRow(self.h2)
        layout.addRow(self.h3)
        layout.addRow(self.h4)
        layout.addRow(self.h5)
        layout.addRow(self.progressHeading)
        layout.addWidget(self.pb3)
        self.tab3.setLayout(layout)

    def condition1(self, percentage):
        if self.check1.isChecked():
            percentage += 20
        if self.check2.isChecked():
            percentage += 20
        if self.check3.isChecked():
            percentage += 20
        if self.check4.isChecked():
            percentage += 20
        if self.check5.isChecked():
            percentage += 20
        self.pb1.setValue(percentage)

    def condition2(self, percentage):
        if self.check6.isChecked():
            percentage += 20
        if self.check7.isChecked():
            percentage += 20
        if self.check8.isChecked():
            percentage += 20
        if self.check9.isChecked():
            percentage += 20
        if self.check10.isChecked():
            percentage += 20
        self.pb2.setValue(percentage)

    def condition3(self, percentage):
        if self.check11.isChecked():
            percentage += 20
        if self.check12.isChecked():
            percentage += 20
        if self.check13.isChecked():
            percentage += 20
        if self.check14.isChecked():
            percentage += 20
        if self.check15.isChecked():
            percentage += 20
        self.pb3.setValue(percentage)

    def start(self):
        self.thread.start()

    def set_max(self, data):
        self.pb.setMaximum(data)


class AllWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(100, 100, 700, 450)
        self.setWindowTitle('To Do List')

        # put calendar on the top of the window
        self.cal1 = QCalendarWidget(self)
        self.cal1.setGridVisible(True)
        self.cal1.move(20, 50)
        self.cal1.clicked[QDate].connect(self.showDate)

        # add dock widget
        self.dock1 = QDockWidget('Calendar', self)
        self.dock1.setWidget(self.cal1)
        self.dock1.move(105, 120)
        self.dock1.setFloating(True)

        # display today's date
        self.labelDate = QLabel(self)
        date = self.cal1.selectedDate()
        self.labelDate.setText(date.toString())
        self.labelDate.move(125, 210)

    def showDate(self, date):
        self.label.setText(date.toString())


app = QApplication(sys.argv)
aw = AllWidgets()
aw.show()
tab = Tab()
tab.show()
sys.exit(app.exec_())
