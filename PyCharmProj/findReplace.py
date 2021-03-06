# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findReplace.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import re

class Ui_FindAndReplace(object):
    def __init__(self):
        self.poem = "A Rock, A River, A Tree" \
       "Hosts to species long since departed," \
       "Marked the mastodon." \
       "The dinosaur, who left dry tokens" \
       "Of their sojourn here" \
       "On our planet floor," \
       "Any broad alarm of their hastening doom" \
       "Is lost in the gloom of dust and ages."

    def setupUi(self, FindAndReplace):
        FindAndReplace.setObjectName("FindAndReplace")
        FindAndReplace.resize(440, 190)
        self.formLayoutWidget = QtWidgets.QWidget(FindAndReplace)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 271, 143))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.findWhatLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.findWhatLabel.setObjectName("findWhatLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.findWhatLabel)
        self.findWhatLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.findWhatLineEdit.setObjectName("findWhatLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.findWhatLineEdit)
        self.replaceWithLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.replaceWithLabel.setObjectName("replaceWithLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.replaceWithLabel)
        self.replaceWithLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.replaceWithLineEdit.setObjectName("replaceWithLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.replaceWithLineEdit)
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox_2)
        self.syntaxLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.syntaxLabel.setObjectName("syntaxLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.syntaxLabel)
        self.syntaxComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.syntaxComboBox.setIconSize(QtCore.QSize(16, 16))
        self.syntaxComboBox.setObjectName("syntaxComboBox")
        self.syntaxComboBox.addItem("")
        self.syntaxComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.syntaxComboBox)
        self.verticalLayoutWidget = QtWidgets.QWidget(FindAndReplace)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 10, 121, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.findBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.findBtn.setObjectName("findBtn")
        # find index of word
        self.countList = []
        self.findBtn.clicked.connect(self.find)
        self.verticalLayout.addWidget(self.findBtn)

        self.replaceBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.replaceBtn.setObjectName("replaceBtn")
        self.verticalLayout.addWidget(self.replaceBtn)
        # replace the current word
        self.replaceBtn.clicked.connect(self.replace)

        self.replaceAllBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.replaceAllBtn.setObjectName("replaceAllBtn")
        self.verticalLayout.addWidget(self.replaceAllBtn)
        # replace all words
        self.replaceAllBtn.clicked.connect(self.replaceAll)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.closeBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.closeBtn.setObjectName("closeBtn")
        self.verticalLayout.addWidget(self.closeBtn)
        self.line = QtWidgets.QFrame(FindAndReplace)
        self.line.setGeometry(QtCore.QRect(290, 10, 20, 171))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(FindAndReplace)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplace)

    def retranslateUi(self, FindAndReplace):
        _translate = QtCore.QCoreApplication.translate
        FindAndReplace.setWindowTitle(_translate("FindAndReplace", "Find and Replace"))
        self.findWhatLabel.setText(_translate("FindAndReplace", "Find what:"))
        self.replaceWithLabel.setText(_translate("FindAndReplace", "Replace with:"))
        self.checkBox.setText(_translate("FindAndReplace", "Case sensitive"))
        self.checkBox_2.setText(_translate("FindAndReplace", "Whole words"))
        self.syntaxLabel.setText(_translate("FindAndReplace", "Syntax"))
        self.syntaxComboBox.setItemText(0, _translate("FindAndReplace", "Literal Text"))
        self.syntaxComboBox.setItemText(1, _translate("FindAndReplace", "Regular Expression"))
        self.findBtn.setText(_translate("FindAndReplace", "Find"))
        self.replaceBtn.setText(_translate("FindAndReplace", "Replace"))
        self.replaceAllBtn.setText(_translate("FindAndReplace", "Replace All"))
        self.closeBtn.setText(_translate("FindAndReplace", "Close"))

    def find(self):
        word = self.findWhatLineEdit.text()
        textList = self.poem.split()
        self.countList = []
        for idx, w in enumerate(textList):
            if w == word:
                self.countList.append(idx)

    def replaceAll(self):
        self.poem = self.poem.replace(self.findWhatLineEdit.text(), self.replaceWithLineEdit.text())
        # for i in self.countList:
        #     print(i)
        # print(self.poem)

    def replace(self):
        # replace only one word
        self.poem = self.poem.replace(self.findWhatLineEdit.text(), self.replaceWithLineEdit.text(), 1)

