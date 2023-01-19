from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.pushButton_8 = None
        self.plainTextEdit = None
        self.pushButton_7 = None
        self.pushButton_6 = None
        self.pushButton_5 = None
        self.pushButton_4 = None
        self.pushButton_3 = None
        self.pushButton_2 = None
        self.pushButton = None
        self.centralwidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/BackgroundFinal/finalBackground1080.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 110, 167, 72))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-image: url(:/Main-Button/main-button-off1080.png); background-color: transparent;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 110, 160, 73))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(:/Channel-Button/channel-button-off1080.png); background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 110, 146, 73))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(:/Genres-Button/Genres-button-off1080.png); background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 110, 203, 73))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(:/Favourites-Button/favourites-button-off1080.png); background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1480, 100, 203, 79))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "background-image: url(:/Settings-Button/settings-button-off1080.png); background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}\n"
                                        "")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1710, 60, 124, 124))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "background-image: url(:/Usericon-Button/Usericon-button1080.png); background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1030, 90, 80, 80))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(:/Search-Button/search-button1080.png); background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(1110, 100, 341, 61))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
                                         "background-color: transparent;\n"
                                         "border: 2px solid #803CE0;\n"
                                         "color: rgb(255, 162, 0);\n"
                                         "font-family: Arial;\n"
                                         "font: 40pt;\n"
                                         "}\n"
                                         "\n"
                                         "QPlainTextEdit:focus {\n"
                                         " background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                         "}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 0, 171, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
                                        "color: rgb(255, 162, 0);\n"
                                        "font-family: Arial;\n"
                                        "font: 30pt;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 131, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton.raise_()
        self.plainTextEdit.raise_()
        self.pushButton_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TV_SHOW"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "ВЫХОД"))
