from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorizationWindow(object):
    def __init__(self):
        self.AdminAuth = None
        self.label_7 = None
        self.label_4 = None
        self.AdminPass = None
        self.AdminLogin = None
        self.label = None
        self.BackButton = None

    def setupUi(self, AuthorizationWindow):
        AuthorizationWindow.setObjectName("AuthorizationWindow")
        AuthorizationWindow.resize(406, 351)
        self.BackButton = QtWidgets.QPushButton(AuthorizationWindow)
        self.BackButton.setGeometry(QtCore.QRect(140, 310, 111, 31))
        self.BackButton.setObjectName("BackButton")
        self.label = QtWidgets.QLabel(AuthorizationWindow)
        self.label.setGeometry(QtCore.QRect(20, 150, 181, 16))
        self.label.setObjectName("label")
        self.AdminLogin = QtWidgets.QPlainTextEdit(AuthorizationWindow)
        self.AdminLogin.setGeometry(QtCore.QRect(20, 180, 191, 20))
        self.AdminLogin.setObjectName("AdminLogin")
        self.AdminPass = QtWidgets.QPlainTextEdit(AuthorizationWindow)
        self.AdminPass.setGeometry(QtCore.QRect(20, 240, 191, 20))
        self.AdminPass.setObjectName("AdminPass")
        self.label_4 = QtWidgets.QLabel(AuthorizationWindow)
        self.label_4.setGeometry(QtCore.QRect(220, 180, 181, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(AuthorizationWindow)
        self.label_7.setGeometry(QtCore.QRect(220, 240, 181, 16))
        self.label_7.setObjectName("label_7")
        self.AdminAuth = QtWidgets.QPushButton(AuthorizationWindow)
        self.AdminAuth.setGeometry(QtCore.QRect(290, 200, 91, 31))
        self.AdminAuth.setObjectName("AdminAuth")

        self.retranslateUi(AuthorizationWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationWindow)

    def retranslateUi(self, AuthorizationWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthorizationWindow.setWindowTitle(_translate("AuthorizationWindow", "Authorization"))
        self.BackButton.setText(_translate("AuthorizationWindow", "Вернуться назад"))
        self.label.setText(_translate("AuthorizationWindow", "Введите логин и пароль"))
        self.label_4.setText(_translate("AuthorizationWindow", "Логин"))
        self.label_7.setText(_translate("AuthorizationWindow", "Пароль"))
        self.AdminAuth.setText(_translate("AuthorizationWindow", "Авторизация"))
