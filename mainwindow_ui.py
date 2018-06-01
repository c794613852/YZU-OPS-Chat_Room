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
        MainWindow.resize(500, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nickname_label = QtWidgets.QLabel(self.centralwidget)
        self.nickname_label.setGeometry(QtCore.QRect(20, 75, 100, 41))
        self.nickname_label.setObjectName("nickname_label")
        self.changpass_label = QtWidgets.QLabel(self.centralwidget)
        self.changpass_label.setGeometry(QtCore.QRect(20, 120, 100, 41))
        self.changpass_label.setObjectName("changpass_label")
        self.onlinenum_label = QtWidgets.QLabel(self.centralwidget)
        self.onlinenum_label.setGeometry(QtCore.QRect(200, 20, 100, 41))
        self.onlinenum_label.setObjectName("onlinenum_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(385, 70, 100, 45))
        self.login_button.setObjectName("login_button")
        self.updatepass_button = QtWidgets.QPushButton(self.centralwidget)
        self.updatepass_button.setGeometry(QtCore.QRect(335, 120, 150, 45))
        self.updatepass_button.setObjectName("updatepass_button")
        self.chat_line = QtWidgets.QTextBrowser(self.centralwidget)
        self.chat_line.setGeometry(QtCore.QRect(20, 180, 460, 390))
        self.chat_line.setObjectName("chat_line")
        self.message_line = QtWidgets.QLineEdit(self.centralwidget)
        self.message_line.setGeometry(QtCore.QRect(20, 575, 460, 41))
        self.message_line.setObjectName("message_line")
        self.nickname_line = QtWidgets.QLineEdit(self.centralwidget)
        self.nickname_line.setGeometry(QtCore.QRect(80, 70, 140, 45))
        self.nickname_line.setObjectName("nickname_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(230, 70, 140, 45))
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.changepass_line = QtWidgets.QLineEdit(self.centralwidget)
        self.changepass_line.setGeometry(QtCore.QRect(120, 120, 200, 45))
        self.changepass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.changepass_line.setObjectName("changepass_line")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(20, 620, 460, 31))
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
        self.changpass_label.setText(_translate("MainWindow", "chang password"))
        self.onlinenum_label.setText(_translate("MainWindow", "目前連天室有"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.updatepass_button.setText(_translate("MainWindow", "update password"))

