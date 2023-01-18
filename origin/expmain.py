import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from stage1 import Ui_MainWindow
from OtherWindow import Ui_OtherWindow

#app = QApplication([])
#window = Window()
#form = Form()
#form.setupUi(window)
#window.show()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def openOtherWindow(): #Кнопка открытия окна диалога
    global OtherWindow
    OtherWindow = QtWidgets.QDialog()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    MainWindow.close()
    #Dialog.hide()
    OtherWindow.show()

    def returnToMain(): #Кнопка возврата на основное окно
        OtherWindow.close()
        MainWindow.show()
    ui.pushButton.clicked.connect(returnToMain)

ui.pushButton_6.clicked.connect(openOtherWindow)

sys.exit(app.exec())
