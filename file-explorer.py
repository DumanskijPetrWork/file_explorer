import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 170)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 621, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.up_button = QtWidgets.QPushButton(self.widget)
        self.up_button.setObjectName("up_button")
        self.verticalLayout.addWidget(self.up_button)
        self.down_button = QtWidgets.QPushButton(self.widget)
        self.down_button.setObjectName("down_button")
        self.verticalLayout.addWidget(self.down_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.file_path = QtWidgets.QLabel(self.widget)
        self.file_path.setText("")
        self.file_path.setObjectName("file_path")
        self.verticalLayout_3.addWidget(self.file_path)
        self.branches_list = QtWidgets.QComboBox(self.widget)
        self.branches_list.setObjectName("branches_list")
        self.verticalLayout_3.addWidget(self.branches_list)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.up_button.setText(_translate("MainWindow", "UP"))
        self.down_button.setText(_translate("MainWindow", "DOWN"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))


if __name__ == '__main__':
    print('---start---\n')
    app = QtWidgets.QApplication(sys.argv)
    application = Ui_MainWindow()
    application.setupUi()
    application.retranslateUi(())
    application.show()
    sys.exit(app.exec_())
