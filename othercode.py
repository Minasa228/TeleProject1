import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Dialog import Ui_Dialog
from OtherWindow import Ui_OtherWindow

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def openOtherWindow(): #Кнопка открытия окна диалога
    global OtherWindow
    OtherWindow = QtWidgets.QDialog()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    Dialog.close()
    #Dialog.hide()
    OtherWindow.show()

    def returnToMain(): #Кнопка возврата на основное окно
        OtherWindow.close()
        Dialog.show()
    ui.pushButton.clicked.connect(returnToMain)

ui.pushButton.clicked.connect(openOtherWindow)

sys.exit(app.exec())

#####
def Genres_Button():# Кнопка запуска окна выбора жанра
    print("clicked!!!")
form.pushButton_3.clicked.connect(Genres_Button)
def Search_Button():# Кнопка активации поиска
    print("clicked!!!")
    print(form.plainTextEdit.toPlainText())
form.pushButton_7.clicked.connect(Search_Button)
def Settings_Button():# Кнопка запуска окна с настройками
    print("clicked!!!")
form.pushButton_5.clicked.connect(Settings_Button)
def Authorization_Button():# Кнопка запуска окна авторизации
    print("clicked!!!")
form.pushButton_6.clicked.connect(Authorization_Button)