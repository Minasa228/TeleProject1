from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from SettingWindow import Ui_SettingsWindow
import sys

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.loadProducts()
    def loadProducts(self):
        self.ui.TableForEditDatabase.setRowCount(30)
        self.ui.TableForEditDatabase.setColumnCount(3)

        self.ui.TableForEditDatabase.setHorizontalHeaderLabels(('Name','Type','Channel'))

        self.ui.TableForEditDatabase.setItem(0,0,QTableWidgetItem('Во все тяжкие'))
        self.ui.TableForEditDatabase.setItem(0,1,QTableWidgetItem('Сериал'))
        self.ui.TableForEditDatabase.setItem(0,2, QTableWidgetItem('Сериатека'))

        self.ui.TableForEditDatabase.setItem(1, 0, QTableWidgetItem('Офис'))
        self.ui.TableForEditDatabase.setItem(1, 1, QTableWidgetItem('Сериал'))
        self.ui.TableForEditDatabase.setItem(1, 2, QTableWidgetItem('Сериатека'))

        self.ui.TableForEditDatabase.setItem(2, 0, QTableWidgetItem('Клиника'))
        self.ui.TableForEditDatabase.setItem(2, 1, QTableWidgetItem('Сериал'))
        self.ui.TableForEditDatabase.setItem(2, 2, QTableWidgetItem('Сериатека'))

        self.ui.TableForEditDatabase.setItem(3, 0, QTableWidgetItem('Рик и Морти'))
        self.ui.TableForEditDatabase.setItem(3, 1, QTableWidgetItem('Мультфильм'))
        self.ui.TableForEditDatabase.setItem(3, 2, QTableWidgetItem('Гик'))

        self.ui.TableForEditDatabase.setItem(4, 0, QTableWidgetItem('Гравити Фолз'))
        self.ui.TableForEditDatabase.setItem(4, 1, QTableWidgetItem('Мультфильм'))
        self.ui.TableForEditDatabase.setItem(4, 2, QTableWidgetItem('Гик'))

        self.ui.TableForEditDatabase.setItem(5, 0, QTableWidgetItem('Как приручить дракона 2'))
        self.ui.TableForEditDatabase.setItem(5, 1, QTableWidgetItem('Мультфильм'))
        self.ui.TableForEditDatabase.setItem(5, 2, QTableWidgetItem('Гик'))

        self.ui.TableForEditDatabase.setItem(6, 0, QTableWidgetItem('Атака титанов'))
        self.ui.TableForEditDatabase.setItem(6, 1, QTableWidgetItem('Аниме'))
        self.ui.TableForEditDatabase.setItem(6, 2, QTableWidgetItem('АнимеГо'))

        self.ui.TableForEditDatabase.setItem(7, 0, QTableWidgetItem('ReZero'))
        self.ui.TableForEditDatabase.setItem(7, 1, QTableWidgetItem('Аниме'))
        self.ui.TableForEditDatabase.setItem(7, 2, QTableWidgetItem('АнимеГо'))

        self.ui.TableForEditDatabase.setItem(8, 0, QTableWidgetItem('Необъятный океан'))
        self.ui.TableForEditDatabase.setItem(8, 1, QTableWidgetItem('Аниме'))
        self.ui.TableForEditDatabase.setItem(8, 2, QTableWidgetItem('АнимеГо'))

        self.ui.TableForEditDatabase.setItem(9, 0, QTableWidgetItem('Триггер'))
        self.ui.TableForEditDatabase.setItem(9, 1, QTableWidgetItem('Драма'))
        self.ui.TableForEditDatabase.setItem(9, 2, QTableWidgetItem('DoДрама'))

        self.ui.TableForEditDatabase.setItem(10, 0, QTableWidgetItem('Брат'))
        self.ui.TableForEditDatabase.setItem(10, 1, QTableWidgetItem('Драма'))
        self.ui.TableForEditDatabase.setItem(10, 2, QTableWidgetItem('DoДрама'))

        self.ui.TableForEditDatabase.setItem(11, 0, QTableWidgetItem('Бойцовский клуб'))
        self.ui.TableForEditDatabase.setItem(11, 1, QTableWidgetItem('Драма'))
        self.ui.TableForEditDatabase.setItem(11, 2, QTableWidgetItem('DoДрама'))

        self.ui.TableForEditDatabase.setItem(12, 0, QTableWidgetItem('Остров проклятых'))
        self.ui.TableForEditDatabase.setItem(12, 1, QTableWidgetItem('Триллер'))
        self.ui.TableForEditDatabase.setItem(12, 2, QTableWidgetItem('ТВ33'))

        self.ui.TableForEditDatabase.setItem(13, 0, QTableWidgetItem('Джон Уик 2'))
        self.ui.TableForEditDatabase.setItem(13, 1, QTableWidgetItem('Триллер'))
        self.ui.TableForEditDatabase.setItem(13, 2, QTableWidgetItem('ТВ33'))

        self.ui.TableForEditDatabase.setItem(14, 0, QTableWidgetItem('Гнев Человеческий'))
        self.ui.TableForEditDatabase.setItem(14, 1, QTableWidgetItem('Триллер'))
        self.ui.TableForEditDatabase.setItem(14, 2, QTableWidgetItem('ТВ33'))

        self.ui.TableForEditDatabase.setItem(15, 0, QTableWidgetItem('Достать ножи'))
        self.ui.TableForEditDatabase.setItem(15, 1, QTableWidgetItem('Детектив'))
        self.ui.TableForEditDatabase.setItem(15, 2, QTableWidgetItem('Слежка'))

        self.ui.TableForEditDatabase.setItem(16, 0, QTableWidgetItem('Шестое чувство'))
        self.ui.TableForEditDatabase.setItem(16, 1, QTableWidgetItem('Детектив'))
        self.ui.TableForEditDatabase.setItem(16, 2, QTableWidgetItem('Слежка'))

        self.ui.TableForEditDatabase.setItem(17, 0, QTableWidgetItem('Сверхъестественно'))
        self.ui.TableForEditDatabase.setItem(17, 1, QTableWidgetItem('Детектив'))
        self.ui.TableForEditDatabase.setItem(17, 2, QTableWidgetItem('Слежка'))

        self.ui.TableForEditDatabase.setItem(18, 0, QTableWidgetItem('Один дома'))
        self.ui.TableForEditDatabase.setItem(18, 1, QTableWidgetItem('Комедия'))
        self.ui.TableForEditDatabase.setItem(18, 2, QTableWidgetItem('Шут'))

        self.ui.TableForEditDatabase.setItem(19, 0, QTableWidgetItem('Всегда говори да'))
        self.ui.TableForEditDatabase.setItem(19, 1, QTableWidgetItem('Комедия'))
        self.ui.TableForEditDatabase.setItem(19, 2, QTableWidgetItem('Шут'))

        self.ui.TableForEditDatabase.setItem(20, 0, QTableWidgetItem('Эйс Вентура'))
        self.ui.TableForEditDatabase.setItem(20, 1, QTableWidgetItem('Комедия'))
        self.ui.TableForEditDatabase.setItem(20, 2, QTableWidgetItem('Шут'))

        self.ui.TableForEditDatabase.setItem(21, 0, QTableWidgetItem('Поезд в Пусан'))
        self.ui.TableForEditDatabase.setItem(21, 1, QTableWidgetItem('Ужасы'))
        self.ui.TableForEditDatabase.setItem(21, 2, QTableWidgetItem('Fear'))

        self.ui.TableForEditDatabase.setItem(22, 0, QTableWidgetItem('Обитель зла'))
        self.ui.TableForEditDatabase.setItem(22, 1, QTableWidgetItem('Ужасы'))
        self.ui.TableForEditDatabase.setItem(22, 2, QTableWidgetItem('Fear'))

        self.ui.TableForEditDatabase.setItem(23, 0, QTableWidgetItem('Сонная лощина'))
        self.ui.TableForEditDatabase.setItem(23, 1, QTableWidgetItem('Ужасы'))
        self.ui.TableForEditDatabase.setItem(23, 2, QTableWidgetItem('Fear'))

        self.ui.TableForEditDatabase.setItem(24, 0, QTableWidgetItem('Пираты карибского моря'))
        self.ui.TableForEditDatabase.setItem(24, 1, QTableWidgetItem('Боевик'))
        self.ui.TableForEditDatabase.setItem(24, 2, QTableWidgetItem('Battle24'))

        self.ui.TableForEditDatabase.setItem(25, 0, QTableWidgetItem('Хоббит'))
        self.ui.TableForEditDatabase.setItem(25, 1, QTableWidgetItem('Боевик'))
        self.ui.TableForEditDatabase.setItem(25, 2, QTableWidgetItem('Battle24'))

        self.ui.TableForEditDatabase.setItem(26, 0, QTableWidgetItem('Звёздные войны'))
        self.ui.TableForEditDatabase.setItem(26, 1, QTableWidgetItem('Боевик'))
        self.ui.TableForEditDatabase.setItem(26, 2, QTableWidgetItem('Battle24'))

        self.ui.TableForEditDatabase.setItem(27, 0, QTableWidgetItem('Футболл: Россия - франция'))
        self.ui.TableForEditDatabase.setItem(27, 1, QTableWidgetItem('Спорт'))
        self.ui.TableForEditDatabase.setItem(27, 2, QTableWidgetItem('Матч'))

        self.ui.TableForEditDatabase.setItem(28, 0, QTableWidgetItem('Футболл: Россия - франция'))
        self.ui.TableForEditDatabase.setItem(28, 1, QTableWidgetItem('Спорт'))
        self.ui.TableForEditDatabase.setItem(28, 2, QTableWidgetItem('Матч'))

        self.ui.TableForEditDatabase.setItem(29, 0, QTableWidgetItem('Футболл: Россия - франция'))
        self.ui.TableForEditDatabase.setItem(29, 1, QTableWidgetItem('Спорт'))
        self.ui.TableForEditDatabase.setItem(29, 2, QTableWidgetItem('Матч'))



def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec())

create_app()