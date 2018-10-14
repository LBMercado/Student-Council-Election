# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.setFixedSize(453, 451)
        self.label = QtWidgets.QLabel(Registration)
        self.label.setGeometry(QtCore.QRect(160, 10, 151, 51))
        self.font = QtGui.QFont()
        self.font.setFamily("Times New Roman")
        self.font.setPointSize(20)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.label.setFont(self.font)
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(Registration)
        self.lineEditName.setGeometry(QtCore.QRect(70, 100, 321, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditEmail = QtWidgets.QLineEdit(Registration)
        self.lineEditEmail.setGeometry(QtCore.QRect(70, 170, 321, 31))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPassword = QtWidgets.QLineEdit(Registration)
        self.lineEditPassword.setGeometry(QtCore.QRect(70, 240, 321, 31))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditReenterPassword = QtWidgets.QLineEdit(Registration)
        self.lineEditReenterPassword.setGeometry(QtCore.QRect(70, 310, 321, 31))
        self.lineEditReenterPassword.setObjectName("lineEditReenterPassword")
        self.pushButtonRegister = QtWidgets.QPushButton(Registration)
        self.pushButtonRegister.setGeometry(QtCore.QRect(70, 380, 321, 31))
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.font.setPointSize(13)
        self.pushButtonRegister.setFont(self.font)
        self.font.setPointSize(15)
        self.lineEditName.setFont(self.font)
        self.lineEditEmail.setFont(self.font)
        self.lineEditPassword.setFont(self.font)
        self.lineEditReenterPassword.setFont(self.font)
        self.lineEditEmail.setStyleSheet("color: gray")
        self.lineEditName.setStyleSheet("color: gray")
        self.lineEditPassword.setStyleSheet("color: gray")
        self.lineEditReenterPassword.setStyleSheet("color: gray")
        self.lineEditEmail.setPlaceholderText("someone@mymail.mapua.edu.ph")
        self.lineEditName.setPlaceholderText("Last name, Given name MI")
        self.lineEditPassword.setPlaceholderText("Password")
        self.lineEditReenterPassword.setPlaceholderText("Re-enter password")
        
        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)
        directory = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        directory = directory.replace("\\", "/")
        background = ("QWidget#Registration{background-image: url(\""+directory
                            +"/Resources/LogInBackground.jpg\"); background-position: center;}")
        Registration.setWindowIcon(QtGui.QIcon((os.path.normpath(os.getcwd() + os.sep + os.pardir))
                                + "\Resources\MapuaIcon.png"))
        Registration.setStyleSheet(background + open((os.path.normpath(os.getcwd() + os.sep + os.pardir)) +
                                         "\Resources\Design.qss",'r').read())
        self.lineEditName.setCursorPosition(0)
        
    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Mapua University"))
        self.label.setText(_translate("Registration", "Registration"))
        self.pushButtonRegister.setText(_translate("Registration", "Register Now"))
        self.pushButtonRegister.clicked.connect(self.register)
        self.lineEditEmail.textChanged.connect(self.inputEmail)
        self.lineEditName.textChanged.connect(self.inputName)
        self.lineEditPassword.textChanged.connect(self.inputPass)
        self.lineEditReenterPassword.textChanged.connect(self.inputRPass)
        
    def register(self): #WHEN REGISTER BUTTON IS CLICKED
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle("SUCCESS")
        mess.setText("WELCOME")
        mess.setWindowIcon(QtGui.QIcon((os.path.normpath(os.getcwd() + os.sep + os.pardir) 
            + "Resources\icon.png")))
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
         
    def inputEmail(self):
        self.lineEditEmail.setStyleSheet("color: white")
        if self.lineEditEmail.text() == "":
            self.lineEditEmail.setStyleSheet("color: gray")
    def inputName(self):
        self.lineEditName.setStyleSheet("color: white")
        if self.lineEditName.text() == "":
            self.lineEditName.setStyleSheet("color: gray")
    def inputPass(self):
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setStyleSheet("color: white")
        if self.lineEditPassword.text() == "":
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPassword.setStyleSheet("color: gray")
    def inputRPass(self):
        self.lineEditReenterPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditReenterPassword.setStyleSheet("color: white")
        if self.lineEditReenterPassword.text() == "":
            self.lineEditReenterPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditReenterPassword.setStyleSheet("color: gray")
              
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QWidget()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())

