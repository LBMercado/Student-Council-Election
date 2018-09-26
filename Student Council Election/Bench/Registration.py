# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ClickableLineEdit(QtWidgets.QLineEdit):
    clicked = QtCore.pyqtSignal() 
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton: self.clicked.emit()

class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(453, 451)
        self.label = QtWidgets.QLabel(Registration)
        self.label.setGeometry(QtCore.QRect(160, 10, 151, 51))
        self.font = QtGui.QFont()
        self.font.setFamily("Times New Roman")
        self.font.setPointSize(20)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.label.setFont(self.font)
        self.label.setObjectName("label")
        self.lineEditName = ClickableLineEdit(Registration)
        self.lineEditName.setGeometry(QtCore.QRect(70, 100, 321, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditEmail = ClickableLineEdit(Registration)
        self.lineEditEmail.setGeometry(QtCore.QRect(70, 170, 321, 31))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPassword = ClickableLineEdit(Registration)
        self.lineEditPassword.setGeometry(QtCore.QRect(70, 240, 321, 31))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditReenterPassword = ClickableLineEdit(Registration)
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
        self.lineEditName.setStyleSheet("color: gray")
        self.lineEditName.setText("Last name, Given name MI")
        self.lineEditEmail.setStyleSheet("color: gray")
        self.lineEditEmail.setText("someone@mymail.mapua.edu.ph")
        self.lineEditPassword.setStyleSheet("color: gray")
        self.lineEditPassword.setText("Password")
        self.lineEditReenterPassword.setStyleSheet("color: gray")
        self.lineEditReenterPassword.setText("Re-enter password")
        
        self.emptyName = True
        self.emptyEmail = True
        self.emptyPassword = True
        self.emptyReenterPassword = True
        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)
        Registration.setWindowIcon(QtGui.QIcon("MapuaIcon.png"))
        Registration.setStyleSheet(open("Design.qss",'r').read())
        self.lineEditName.setCursorPosition(0)
        
    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Mapua University"))
        self.label.setText(_translate("Registration", "Registration"))
        self.pushButtonRegister.setText(_translate("Registration", "Register Now"))
        self.lineEditName.clicked.connect(self.nameClicked)
        self.lineEditEmail.clicked.connect(self.emailClicked)
        self.lineEditPassword.clicked.connect(self.passwordClicked)
        self.lineEditReenterPassword.clicked.connect(self.reenterPasswordClicked)
        self.lineEditName.textEdited.connect(self.removeName)
        self.lineEditEmail.textEdited.connect(self.removeEmail)
        self.lineEditPassword.textEdited.connect(self.removePassword)
        self.lineEditReenterPassword.textEdited.connect(self.removeReenterPassword)
        self.lineEditName.editingFinished.connect(self.resetName)
        self.lineEditEmail.editingFinished.connect(self.resetEmail)
        self.lineEditPassword.editingFinished.connect(self.resetPassword)
        self.lineEditReenterPassword.editingFinished.connect(self.resetReenterPassword)
        self.pushButtonRegister.clicked.connect(self.register)
        
    def register(self): #WHEN REGISTER BUTTON IS CLICKED
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle("SUCCESS")
        mess.setText("WELCOME")
        mess.setWindowIcon(QtGui.QIcon("icon.png"))
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def resetName(self):
        if len(self.lineEditName.text()) == 0:
            self.emptyName = True
        if self.emptyName:
            self.lineEditName.setStyleSheet("color: gray;")
            self.lineEditName.setText("Last name, Given name MI")    
    def resetEmail(self):
        if len(self.lineEditEmail.text()) == 0:
            self.emptyEmail = True
        if self.emptyEmail:
            self.lineEditEmail.setStyleSheet("color: gray;")
            self.lineEditEmail.setText("someone@mymail.mapua.edu.ph")    
    def resetPassword(self):
        if len(self.lineEditPassword.text()) == 0:
            self.emptyPassword = True
        if self.emptyPassword:
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPassword.setStyleSheet("color: gray;")
            self.lineEditPassword.setText("Password")    
    def resetReenterPassword(self):
        if len(self.lineEditReenterPassword.text()) == 0:
            self.emptyReenterPassword = True
        if self.emptyReenterPassword:
            self.lineEditReenterPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditReenterPassword.setStyleSheet("color: gray;")
            self.lineEditReenterPassword.setText("Re-enter password")    
                   
    def removeName(self):
        if self.emptyName:
            self.emptyName = False
            self.lineEditName.setStyleSheet("color: white;")
            self.lineEditName.setText(self.lineEditName.text()[0])
    def removeEmail(self):
        if self.emptyEmail:
            self.emptyEmail = False
            self.lineEditEmail.setStyleSheet("color: white;")
            self.lineEditEmail.setText(self.lineEditEmail.text()[0])
    def removePassword(self):
        if self.emptyPassword:
            self.emptyPassword = False
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            self.lineEditPassword.setStyleSheet("color: white;")
            self.lineEditPassword.setText(self.lineEditPassword.text()[0])
    def removeReenterPassword(self):
        if self.emptyReenterPassword:
            self.emptyReenterPassword = False
            self.lineEditReenterPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            self.lineEditReenterPassword.setStyleSheet("color: white;")
            self.lineEditReenterPassword.setText(self.lineEditReenterPassword.text()[0])
                  
    def nameClicked(self):
        if self.lineEditName.text() == "Last name, Given name MI":
            self.lineEditName.setCursorPosition(0)
    def emailClicked(self):
        if self.lineEditEmail.text() == "someone@mymail.mapua.edu.ph":
            self.lineEditEmail.setCursorPosition(0)  
    def passwordClicked(self):
        if self.lineEditPassword.text() == "Password":
            self.lineEditPassword.setCursorPosition(0)      
    def reenterPasswordClicked(self):
        if self.lineEditReenterPassword.text() == "Re-enter password":
            self.lineEditReenterPassword.setCursorPosition(0)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QWidget()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())

