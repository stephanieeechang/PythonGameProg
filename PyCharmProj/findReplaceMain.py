import sys
from PyQt5.QtWidgets import QApplication, QDialog
# import converted UI
from findReplace import Ui_FindAndReplace

# create an QT application
app = QApplication(sys.argv)
# create a dialog window
window = QDialog()
# create a findAndReplace dialog (object)
ui = Ui_FindAndReplace()
# add the findAndReplace dialog to the main window
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
