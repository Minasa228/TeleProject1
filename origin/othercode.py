import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Dialog import Ui_Dialog
from OtherWindow import Ui_OtherWindow

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def openOtherWindow():
    global OtherWindow
    OtherWindow = QtWidgets.QDialog()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    Dialog.close()
    #Dialog.hide()
    OtherWindow.show()

    def returnToMain():
        OtherWindow.close()
        Dialog.show()

    ui.pushButton.clicked.connect(returnToMain)

ui.pushButton.clicked.connect(openOtherWindow)

sys.exit(app.exec())
