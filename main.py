from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_MainWindow
import Background_rc

# Создать приложение
app = QtGui.QGuiApplication(sys.argv)

# Создать форму и инициализировать Ui
Form = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
Form.show()
# Логика приложения


# Запустить Логику
sys.exit(app.exec_())