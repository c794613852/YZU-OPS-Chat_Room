# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc01\Desktop\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nickname_label = QtWidgets.QLabel(self.centralwidget)
        self.nickname_label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.nickname_label.setObjectName("nickname_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(240, 10, 111, 61))
        self.login_button.setObjectName("login_button")
        self.chat_line = QtWidgets.QTextBrowser(self.centralwidget)
        self.chat_line.setGeometry(QtCore.QRect(20, 80, 331, 401))
        self.chat_line.setObjectName("chat_line")
        self.message_line = QtWidgets.QLineEdit(self.centralwidget)
        self.message_line.setGeometry(QtCore.QRect(20, 490, 331, 41))
        self.message_line.setObjectName("message_line")
        self.nickname_line = QtWidgets.QLineEdit(self.centralwidget)
        self.nickname_line.setGeometry(QtCore.QRect(110, 10, 113, 61))
        self.nickname_line.setObjectName("nickname_line")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(20, 540, 331, 31))
        self.send_button.setObjectName("send_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat Application"))
        self.nickname_label.setText(_translate("MainWindow", "Nick Name"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.send_button.setText(_translate("MainWindow", "Send"))

