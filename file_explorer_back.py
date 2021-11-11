import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QColor
from PyQt5.QtWidgets import QMessageBox
from file_explorer import Ui_MainWindow
from file_tree import *


class BackEnd(QtWidgets.QMainWindow):
    styleSheet_white = "background-color : white"
    styleSheet_gray = "background-color : gray"

    def __init__(self):
        super(BackEnd, self).__init__()
        self._front_end = Ui_MainWindow()
        self._front_end.setupUi(self)
        self.init_FrontEnd()

        self.os_tree = FileTree('/Users/dumanskij/Документы mac')
        self.os_tree.build_tree()

        self.reset_info()

    # Инициализация функционала
    def init_FrontEnd(self):
        # Текст кнопок
        self._front_end.up_button.setText("UP")
        self._front_end.down_button.setText("DOWN")
        self._front_end.pushButton_3.setText("DELETE")

        # Обработка нажатий на кнопки
        self._front_end.up_button.clicked.connect(self.up_button_pressed)
        self._front_end.down_button.clicked.connect(self.down_button_pressed)
        self._front_end.pushButton_3.clicked.connect(self.pushButton_3_pressed)

        # Начальная обработка кнопок
        self._front_end.up_button.setStyleSheet(self.styleSheet_gray)
        self._front_end.down_button.setStyleSheet(self.styleSheet_white)

        # Окно предупреждения
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Доступ запрещен")
        self.msg.setInformativeText("Невозможно удалить файл / директорию")
        self.msg.setStandardButtons(QMessageBox.Ok)

    # Обновление информации
    def reset_info(self):
        self._front_end.file_path.setText('   ' + self.os_tree.current_path)
        self._front_end.branches_list.clear()
        model_branches_list = self._front_end.branches_list.model()
        if path.isdir(self.os_tree.current_path):
            for name in self.os_tree.current.branches:
                item = QStandardItem(name)
                item.setBackground(QColor('white'))
                model_branches_list.appendRow(item)
        # self._front_end.branches_list.addItems(self.os_tree.current.branches)

    # Движение вверх
    def up_button_pressed(self):
        if self.os_tree.is_there_path_up():
            print('поменять цвет кнопки UP на белый')  # Если цвет кнопки не белый
            self._front_end.up_button.setStyleSheet(self.styleSheet_white)

            self.os_tree.path_up()
            self.reset_info()

            print('поменять цвет кнопки DOWN на белый')  # Если цвет кнопки не белый
            self._front_end.down_button.setStyleSheet(self.styleSheet_white)

        if not self.os_tree.is_there_path_up():  # Двойная проверка (else + после действия)
            print('поменять цвет кнопки UP на серый')  # Если цвет кнопки не серый
            self._front_end.up_button.setStyleSheet(self.styleSheet_gray)

        if self.os_tree.current == self.os_tree.root:
            self._front_end.pushButton_3.setStyleSheet(self.styleSheet_gray)

    # Движение вниз
    def down_button_pressed(self):
        if self.os_tree.is_there_path_down():
            print('поменять цвет кнопки DOWN на белый')  # Если цвет кнопки не белый
            self._front_end.down_button.setStyleSheet(self.styleSheet_white)

            self.os_tree.path_down(self._front_end.branches_list.currentText())
            self.reset_info()

            print('поменять цвет кнопки UP на белый')  # Если цвет кнопки не белый
            self._front_end.up_button.setStyleSheet(self.styleSheet_white)

        if not self.os_tree.is_there_path_down():  # Двойная проверка (else + после действия)
            print('поменять цвет кнопки DOWN на серый')  # Если цвет кнопки не серый
            self._front_end.down_button.setStyleSheet(self.styleSheet_gray)

        if self.os_tree.current != self.os_tree.root:
            self._front_end.pushButton_3.setStyleSheet(self.styleSheet_white)

    # Удаление файла / директории
    def pushButton_3_pressed(self):
        _file = self.os_tree.current
        if _file != self.os_tree.root:
            self._front_end.pushButton_3.setStyleSheet(self.styleSheet_white)
            try:
                self.os_tree.delete_node(_file)
                self.reset_info()
            except OSError:
                self.msg.show()
        if self.os_tree.current == self.os_tree.root:
            self._front_end.pushButton_3.setStyleSheet(self.styleSheet_gray)

if __name__ == '__main__':
    print('-----start-----\n')
    app = QtWidgets.QApplication(sys.argv)
    application = BackEnd()
    application.show()
    sys.exit(app.exec_())
