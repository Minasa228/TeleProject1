from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import authorization_uiEXP
import sys
class Authorization(QMainWindow, authorization_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Authorization()
    form.show()
    app.exec()