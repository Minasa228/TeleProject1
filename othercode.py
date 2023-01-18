import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from stage1 import Ui_MainWindow
from AuthorizationWindow import Ui_AuthorizationWindow
from GenreWindow import Ui_GenreWindow
from SettingWindow import Ui_SettingsWindow

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

def Genre_Button_openOtherWindow():# Кнопка запуска окна выбора жанра
    global GenreWindow
    GenreWindow = QtWidgets.QDialog()
    ui = Ui_GenreWindow()
    ui.setupUi(GenreWindow)
    MainWindow.close()
    # Dialog.hide()
    GenreWindow.show()
    def returnToMain():  # Кнопка возврата на основное окно
        GenreWindow.close()
        MainWindow.show()
    ui.BackButton.clicked.connect(returnToMain)
ui.pushButton_3.clicked.connect(Genre_Button_openOtherWindow)

def Search_Button():# Кнопка активации поиска
    print("clicked!!!")
    print(ui.plainTextEdit.toPlainText())
ui.pushButton_7.clicked.connect(Search_Button)
def Settings_Button_openOtherWindow():# Кнопка запуска окна с настройками
    global SettingsWindow
    SettingsWindow = QtWidgets.QDialog()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    MainWindow.close()
    # Dialog.hide()
    SettingsWindow.show()
class
    def __init__(self):

    self.loadProducts()
    def loadProducts(self)
    def returnToMain():  # Кнопка возврата на основное окно
        SettingsWindow.close()
        MainWindow.show()
    ui.BackButton.clicked.connect(returnToMain)

ui.pushButton_5.clicked.connect(Settings_Button_openOtherWindow)

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

