import sys
from PyQt5.QtWidgets import QApplication, QDialog
from findReplace import Ui_FindAndReplace

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_FindAndReplace()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
