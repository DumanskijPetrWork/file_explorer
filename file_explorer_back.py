import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QColor
from file_explorer import Ui_MainWindow
from file_tree import *


class BackEnd(QtWidgets.QMainWindow):
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
        self.os_tree.path_up()
        self.reset_info()

    # Движение вниз

    def down_button_pressed(self):
        self.os_tree.path_down(self._front_end.branches_list.currentText())
        self.reset_info()

    # Удаление файла / директории

    def pushButton_3_pressed(self):
        self.os_tree.delete_node()
        self.reset_info()


if __name__ == '__main__':
    print('-----start-----\n')
    app = QtWidgets.QApplication(sys.argv)
    application = BackEnd()
    application.show()
    sys.exit(app.exec_())
