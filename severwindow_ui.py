# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc01\Desktop\severwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SeverWindow(object):
    def setupUi(self, SeverWindow):
        SeverWindow.setObjectName("SeverWindow")
        SeverWindow.resize(348, 610)
        self.centralwidget = QtWidgets.QWidget(SeverWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nickname_label = QtWidgets.QLabel(self.centralwidget)
        self.nickname_label.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.nickname_label.setLineWidth(1)
        self.nickname_label.setTextFormat(QtCore.Qt.AutoText)
        self.nickname_label.setObjectName("nickname_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(170, 10, 51, 16))
        self.password_label.setObjectName("password_label")
        self.nickname_line = QtWidgets.QLineEdit(self.centralwidget)
        self.nickname_line.setGeometry(QtCore.QRect(60, 10, 101, 21))
        self.nickname_line.setObjectName("nickname_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(220, 10, 111, 20))
        self.password_line.setInputMask("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 321, 431))
        self.textBrowser.setObjectName("textBrowser")
        self.del_button = QtWidgets.QPushButton(self.centralwidget)
        self.del_button.setGeometry(QtCore.QRect(10, 555, 150, 30))
        self.del_button.setObjectName("del_button")
        self.kick_button = QtWidgets.QPushButton(self.centralwidget)
        self.kick_button.setGeometry(QtCore.QRect(180, 555, 150, 30))
        self.kick_button.setObjectName("kick_button")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(10, 40, 321, 31))
        self.user_line = QtWidgets.QLineEdit(self.centralwidget)
        self.user_line.setGeometry(QtCore.QRect(10, 520, 321, 30))
        self.user_line.setObjectName("user_line")
        self.add_button.setObjectName("add_button")
        SeverWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SeverWindow)
        self.statusbar.setObjectName("statusbar")
        SeverWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SeverWindow)
        QtCore.QMetaObject.connectSlotsByName(SeverWindow)

    def retranslateUi(self, SeverWindow):
        _translate = QtCore.QCoreApplication.translate
        SeverWindow.setWindowTitle(_translate("SeverWindow", "Chat Application"))
        self.nickname_label.setText(_translate("SeverWindow", "NickName"))
        self.password_label.setText(_translate("SeverWindow", "Password"))
        self.del_button.setText(_translate("SeverWindow", "Del"))
        self.kick_button.setText(_translate("SeverWindow", "Kick"))
        self.add_button.setText(_translate("SeverWindow", "Add"))

