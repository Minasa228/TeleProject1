import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from stage1 import Ui_MainWindow
from AuthorizationWindow import Ui_AuthorizationWindow

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

def Genres_Button():# Кнопка запуска окна выбора жанра
    print("clicked!!!")
ui.pushButton_3.clicked.connect(Genres_Button)
def Search_Button():# Кнопка активации поиска
    print("clicked!!!")
    print(ui.plainTextEdit.toPlainText())
ui.pushButton_7.clicked.connect(Search_Button)
def Settings_Button():# Кнопка запуска окна с настройками
    print("clicked!!!")
ui.pushButton_5.clicked.connect(Settings_Button)

def Authorization_Button_openOtherWindow(): #Кнопка открытия окна диалога
    global AuthorizationWindow
    AuthorizationWindow = QtWidgets.QDialog()
    ui = Ui_AuthorizationWindow()
    ui.setupUi(AuthorizationWindow)
    MainWindow.close()
    #Dialog.hide()
    AuthorizationWindow.show()

    def returnToMain(): #Кнопка возврата на основное окно
        AuthorizationWindow.close()
        MainWindow.show()
    ui.BackButton.clicked.connect(returnToMain)

ui.pushButton_6.clicked.connect(Authorization_Button_openOtherWindow)



sys.exit(app.exec())

