from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from SettingWindow import Ui_SettingsWindow
import sys

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.loadProducts(self)

    def load
        self.ui.TableForEditDatabase

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec())

create_app()