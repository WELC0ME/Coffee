# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 460)
        MainWindow.setMinimumSize(QtCore.QSize(520, 460))
        MainWindow.setMaximumSize(QtCore.QSize(520, 460))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 500, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(10, 420, 245, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_remove = QtWidgets.QPushButton(self.centralwidget)
        self.btn_remove.setGeometry(QtCore.QRect(265, 420, 245, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_remove.setFont(font)
        self.btn_remove.setObjectName("btn_remove")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.btn_remove.setText(_translate("MainWindow", "Remove"))
