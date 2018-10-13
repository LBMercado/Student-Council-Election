# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.Registration import Ui_Registration
from UI.StudentCouncilElection import Ui_StudentCouncilElection
from UI.Admin import Ui_Admin
from BusinessLogic.UserInterface import UserInterface
from BusinessLogic.Election import Election
from BusinessLogic.Admin import Admin

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        #   custom variables
        self.LogIn = LogIn
        self.userInterface = UserInterface()
        self.election = None
        self.projDirectory = os.getcwd()

        LogIn.setObjectName("LogIn")
        LogIn.setFixedSize(630, 507)
#        LogIn.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.pushButtonLogin = QtWidgets.QPushButton(LogIn)
        self.pushButtonLogin.setGeometry(QtCore.QRect(320, 340, 290, 51))
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonLogin.setAutoDefault(True)
        self.lineEditUsername = QtWidgets.QLineEdit(LogIn)
        self.lineEditUsername.setGeometry(QtCore.QRect(320, 220, 290, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setText("")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(LogIn)
        self.lineEditPassword.setGeometry(QtCore.QRect(320, 260, 290, 31))
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonCreateAccount = QtWidgets.QPushButton(LogIn)
        self.pushButtonCreateAccount.setGeometry(QtCore.QRect(320, 402, 290, 31))
        self.pushButtonCreateAccount.setObjectName("pushButtonCreateAccount")
        self.pushButtonCreateAccount.setAutoDefault(True)
        font.setPointSize(15)
        self.pushButtonLogin.setFont(font)
        self.labelErrorIcon = QtWidgets.QLabel(LogIn)
        self.labelErrorIcon.setGeometry(320, 298, 25, 25)
        self.labelErrorIcon.setObjectName("labelErrorIcon")
        self.labelError = QtWidgets.QLabel(LogIn)
        self.labelError.setGeometry(355, 295, 200, 30)
        self.labelError.setObjectName("labelError")
        font.setPointSize(12)
        self.labelError.setFont(font)
        self.label = QtWidgets.QLabel(LogIn)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.labelMapuaLogo = QtWidgets.QLabel(LogIn)
        self.labelMapuaLogo.setObjectName("labelMapuaLogo")
        self.labelMapuaLogo.setGeometry(390,45,150,150)
        pic = QtGui.QPixmap(self.projDirectory + "\Resources\MapuaLogo.png")
        self.labelMapuaLogo.setPixmap(pic)
        projDirectory = self.projDirectory.replace("\\", "/")
        background = ("QWidget#LogIn{background-image: url(\""+ projDirectory
                            +"/Resources/LogInBackground.jpg\"); background-position: center;}")
        LogIn.setStyleSheet(background + open(self.projDirectory
        + "\Resources\Design.qss",'r').read())
        self.StudentCouncilElection = QtWidgets.QWidget()
        self.ui = Ui_StudentCouncilElection()
        self.ui.setupUi(self.StudentCouncilElection)
        self.Admin = QtWidgets.QWidget()
        self.uiAdmin = Ui_Admin()
        self.uiAdmin.setupUi(self.Admin)
        self.retranslateUi(LogIn)
        
        self.lineEditPassword.setStyleSheet("color: gray")
        self.lineEditUsername.setStyleSheet("color: gray")
        self.lineEditPassword.setPlaceholderText("Password")
        self.lineEditUsername.setPlaceholderText("someone@mymail.mapua.edu.ph")
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        LogIn.setTabOrder(self.lineEditUsername, self.lineEditPassword)
        LogIn.setTabOrder(self.lineEditPassword, self.pushButtonLogin)
        LogIn.setTabOrder(self.pushButtonLogin, self.pushButtonCreateAccount)
        LogIn.setWindowIcon(QtGui.QIcon(projDirectory
        + "\Resources\MapuaIcon.png"))      
        
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Mapua University"))
        self.pushButtonLogin.setText(_translate("LogIn", "LOGIN"))
        self.pushButtonCreateAccount.setText(_translate("LogIn", "REGISTER"))
        self.label.setText(_translate("LogIn", "<html><head/><body><p>Welcome </p><p>to the</p><p>Student Council </p><p>Election</p></body></html>"))
        self.pushButtonLogin.clicked.connect(self.logIn)
        self.pushButtonCreateAccount.clicked.connect(self.createAccount)
        self.pushButtonCreateAccount.mouseMoveEvent
        self.lineEditPassword.returnPressed.connect(self.logIn)
        self.lineEditUsername.returnPressed.connect(self.logIn)
        self.lineEditPassword.textChanged.connect(self.inputPass)
        self.lineEditUsername.textChanged.connect(self.inputUser)
        self.ui.pushButtonSignout.clicked.connect(self.reLogIn)
        self.uiAdmin.pushButton.clicked.connect(self.reLogInAdmin)
        
    def logIn(self):
        inputUsername = self.lineEditUsername.text()
        inputPassword = self.lineEditPassword.text()
        self.userInterface.set_user_email_and_password(inputUsername, inputPassword)
        #   there must be an election date for it to continue
        if (not Election.ElectionExists()):
            #   inform user there is no current election
            pic = QtGui.QPixmap(self.projDirectory + "\Resources\errorIcon")
            self.labelErrorIcon.setPixmap(pic)
            #   however, admin can still login, need to check this
            user = self.userInterface.GetUser()
            if self.userInterface.is_User() and self.userInterface.is_Admin():
                user = Admin.morph_user_to_admin(user)
                self.labelError.setText("Admin override.")
                self.uiAdmin.PassAdminInfo(user)
                self.Admin.show()
                self.LogIn.hide()
            else:
                self.labelError.setText("There is no current election in progress.")
                return
        else:
            # an election exists, load an instance of the election from the database
            self.election = Election.init_with_startAndEndDate(Election.GetExistingElectionStartDate(),
                                                               Election.GetExistingElectionEndDate())
            if inputUsername == "":
                pic = QtGui.QPixmap(self.projDirectory + "\Resources\errorIcon")
                self.labelErrorIcon.setPixmap(pic)
                self.labelError.setText("Please enter email.")
            elif inputPassword == "":
                pic = QtGui.QPixmap(self.projDirectory + "\Resources\errorIcon")
                self.labelErrorIcon.setPixmap(pic)
                self.labelError.setText("Please enter password.")
            elif self.userInterface.user_email_is_valid():  # email exists
                if self.userInterface.is_User():  # correct matching password for email
                    #   must check if user is an admin
                    if self.userInterface.is_Admin():
                        user = self.userInterface.GetUser()
                        user = Admin.morph_user_to_admin(user)
                        self.labelError.setText("")
                        self.uiAdmin.PassAdminInfo(user)
                        self.Admin.show()
                        self.LogIn.hide()
                    else:
                        self.StudentCouncilElection.show()
                        self.ui.pass_user_interface(self.userInterface)
                        self.ui.init_election_interface()
                        self.ui.setProfile(inputUsername, inputPassword)
                        self.LogIn.hide()
                else:
                    self.emptyPassword = True
                    self.resetPassword()
                    pic = QtGui.QPixmap(self.projDirectory
                                        + "\Resources\errorIcon")
                    self.labelErrorIcon.setPixmap(pic)
                    self.labelError.setText("Incorrect password.")
            else:
                pic = QtGui.QPixmap(self.projDirectory
                                    + "\Resources\errorIcon")
                self.labelErrorIcon.setPixmap(pic)
                self.labelError.setText("Email does not exist.")
    def createAccount(self):
        self.Registration = QtWidgets.QWidget()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.Registration)
        self.Registration.show()
    def reLogIn(self):
        self.StudentCouncilElection.close()
        self.LogIn.show()
    def inputUser(self):
        self.lineEditUsername.setStyleSheet("color: white")
        if self.lineEditUsername.text() == "":
            self.lineEditUsername.setStyleSheet("color: gray")
    def inputPass(self):
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setStyleSheet("color: white")
        if self.lineEditPassword.text() == "":
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPassword.setStyleSheet("color: gray")

    def resetPassword(self):
        if len(self.lineEditPassword.text()) == 0:
            self.emptyPassword = True
        if self.emptyPassword:
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPassword.setStyleSheet("color: gray;")
            self.lineEditPassword.setText('')
            self.lineEditPassword.setCursorPosition(0)

    def reLogInAdmin(self):
        self.Admin.close()
        self.LogIn.show()