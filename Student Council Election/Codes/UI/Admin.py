# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lauren\Desktop\Admin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from BusinessLogic.Election import Election
from BusinessLogic.AdminInterface import AdminInterface
from BusinessLogic.Admin import Admin
from BusinessLogic.User import User
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Position import Position
from datetime import datetime, timedelta

class Ui_Admin(object):
    def setupUi(self, Admin):
        #   custom variables
        self.election_duration = 10 #   set in program
        self.projDirectory = os.getcwd()

        Admin.setObjectName("Admin")
        Admin.resize(1000, 600)
        self.pushButtonCreateUser = QtWidgets.QPushButton(Admin)
        self.pushButtonCreateUser.setGeometry(QtCore.QRect(50, 100, 150, 50))
        self.pushButtonCreateUser.setObjectName("pushButtonCreateUser")
        self.pushButtonDeleteUser = QtWidgets.QPushButton(Admin)
        self.pushButtonDeleteUser.setGeometry(QtCore.QRect(50, 170, 150, 50))
        self.pushButtonDeleteUser.setObjectName("pushButtonDeleteUser")
        self.pushButtonEditUser = QtWidgets.QPushButton(Admin)
        self.pushButtonEditUser.setGeometry(QtCore.QRect(50, 240, 150, 50))
        self.pushButtonEditUser.setObjectName("pushButtonEditUser")
        self.pushButtonStartElec = QtWidgets.QPushButton(Admin)
        self.pushButtonStartElec.setGeometry(QtCore.QRect(50, 310, 150, 50))
        self.pushButtonStartElec.setObjectName("pushButtonStartElec")
        self.pushButtonEndElec = QtWidgets.QPushButton(Admin)
        self.pushButtonEndElec.setGeometry(QtCore.QRect(50, 380, 150, 50))
        self.pushButtonEndElec.setObjectName("pushButtonEndElec")
        self.pushButtonSummary = QtWidgets.QPushButton(Admin)
        self.pushButtonSummary.setGeometry(QtCore.QRect(50, 450, 150, 50))
        self.pushButtonSummary.setObjectName("pushButtonSummary")
        self.scrollAreaCreateUser = QtWidgets.QScrollArea(Admin)
        self.scrollAreaCreateUser.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaCreateUser.setWidgetResizable(True)
        self.scrollAreaCreateUser.setObjectName("scrollAreaCreateUser")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButtonCreate = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonCreate.setGeometry(QtCore.QRect(270, 330, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonCreate.setFont(font)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.groupBoxUser = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxUser.setGeometry(QtCore.QRect(140, 0, 501, 311))
        self.groupBoxUser.setTitle("")
        self.groupBoxUser.setObjectName("groupBoxUser")
        self.lineEditName = QtWidgets.QLineEdit(self.groupBoxUser)
        self.lineEditName.setGeometry(QtCore.QRect(20, 20, 461, 41))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditStudentNum = QtWidgets.QLineEdit(self.groupBoxUser)
        self.lineEditStudentNum.setGeometry(QtCore.QRect(20, 80, 461, 41))
        self.lineEditStudentNum.setObjectName("lineEditStudentNum")
        self.lineEditPass = QtWidgets.QLineEdit(self.groupBoxUser)
        self.lineEditPass.setGeometry(QtCore.QRect(20, 200, 461, 41))
        self.lineEditPass.setObjectName("lineEditPass")
        self.lineEditReenterPass = QtWidgets.QLineEdit(self.groupBoxUser)
        self.lineEditReenterPass.setGeometry(QtCore.QRect(20, 260, 461, 41))
        self.lineEditReenterPass.setObjectName("lineEditReenterPass")
        self.lineEditProgram = QtWidgets.QLineEdit(self.groupBoxUser)
        self.lineEditProgram.setGeometry(QtCore.QRect(20, 140, 461, 41))
        self.lineEditProgram.setObjectName("lineEditProgram")
        self.groupBoxAdmin = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxAdmin.setGeometry(QtCore.QRect(140, 50, 501, 251))
        self.groupBoxAdmin.setTitle("")
        self.groupBoxAdmin.setObjectName("groupBoxAdmin")
        self.lineEditNameAdmin = QtWidgets.QLineEdit(self.groupBoxAdmin)
        self.lineEditNameAdmin.setGeometry(QtCore.QRect(20, 20, 461, 41))
        self.lineEditNameAdmin.setObjectName("lineEditNameAdmin")
        self.lineEditPassAdmin = QtWidgets.QLineEdit(self.groupBoxAdmin)
        self.lineEditPassAdmin.setGeometry(QtCore.QRect(20, 90, 461, 41))
        self.lineEditPassAdmin.setObjectName("lineEditPassAdmin")
        self.lineEditReenterPassAdmin = QtWidgets.QLineEdit(self.groupBoxAdmin)
        self.lineEditReenterPassAdmin.setGeometry(QtCore.QRect(20, 160, 461, 41))
        self.lineEditReenterPassAdmin.setObjectName("lineEditReenterPassAdmin")
        self.pushButtonUser = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonUser.setGeometry(QtCore.QRect(10, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonUser.setFont(font)
        self.pushButtonUser.setObjectName("pushButtonUser")
        self.pushButtonAdmin = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonAdmin.setGeometry(QtCore.QRect(10, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonAdmin.setFont(font)
        self.pushButtonAdmin.setObjectName("pushButtonAdmin")
        self.scrollAreaCreateUser.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(Admin)
        self.pushButton.setGeometry(QtCore.QRect(910, 20, 51, 51))
        self.pushButton.setObjectName("pushButton")
        self.scrollAreaDelete = QtWidgets.QScrollArea(Admin)
        self.scrollAreaDelete.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaDelete.setWidgetResizable(True)
        self.scrollAreaDelete.setObjectName("scrollAreaDelete")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.lineEditSearch = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEditSearch.setGeometry(QtCore.QRect(60, 40, 461, 41))
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.pushButtonSearch = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButtonSearch.setGeometry(QtCore.QRect(560, 40, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.labelDelProfile = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelDelProfile.setGeometry(QtCore.QRect(60, 120, 581, 171))
        self.labelDelProfile.setWordWrap(True)
        self.labelDelProfile.setObjectName("labelDelProfile")
        self.pushButtonDelete = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButtonDelete.setGeometry(QtCore.QRect(280, 320, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.scrollAreaDelete.setWidget(self.scrollAreaWidgetContents_3)
        self.labelElectionStatus = QtWidgets.QLabel(Admin)
        self.labelElectionStatus.setGeometry(QtCore.QRect(60, 520, 451, 71))
        self.labelElectionStatus.setObjectName("labelElectionStatus")
        self.scrollAreaSumm = QtWidgets.QScrollArea(Admin)
        self.scrollAreaSumm.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaSumm.setWidgetResizable(True)
        self.scrollAreaSumm.setObjectName("scrollAreaSumm")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBoxPosition = QtWidgets.QComboBox(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPosition.sizePolicy().hasHeightForWidth())
        self.comboBoxPosition.setSizePolicy(sizePolicy)
        self.comboBoxPosition.setMaximumSize(QtCore.QSize(400, 40))
        self.comboBoxPosition.setObjectName("comboBoxPosition")
        self.verticalLayout_3.addWidget(self.comboBoxPosition)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(120, 120))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(120, 120))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.scrollAreaSumm.setWidget(self.scrollAreaWidgetContents_5)
        self.scrollAreaEdit = QtWidgets.QScrollArea(Admin)
        self.scrollAreaEdit.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaEdit.setWidgetResizable(True)
        self.scrollAreaEdit.setObjectName("scrollAreaEdit")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.lineEditSearchEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEditSearchEdit.setGeometry(QtCore.QRect(20, 20, 461, 41))
        self.lineEditSearchEdit.setObjectName("lineEditSearchEdit")
        self.pushButtonSearchEdit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButtonSearchEdit.setGeometry(QtCore.QRect(500, 20, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchEdit.setFont(font)
        self.pushButtonSearchEdit.setObjectName("pushButtonSearchEdit")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 281, 151))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButtonEdit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButtonEdit.setGeometry(QtCore.QRect(510, 280, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonEdit.setFont(font)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.lineEditNameEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEditNameEdit.setGeometry(QtCore.QRect(330, 110, 371, 31))
        self.lineEditNameEdit.setObjectName("lineEditNameEdit")
        self.lineEditStudentNumEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEditStudentNumEdit.setGeometry(QtCore.QRect(330, 170, 371, 31))
        self.lineEditStudentNumEdit.setObjectName("lineEditStudentNumEdit")
        self.lineEditPasswordEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEditPasswordEdit.setGeometry(QtCore.QRect(330, 230, 371, 31))
        self.lineEditPasswordEdit.setObjectName("lineEditPasswordEdit")
        self.pushButtonEditPromote = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButtonEditPromote.setGeometry(QtCore.QRect(20, 280, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonEditPromote.setFont(font)
        self.pushButtonEditPromote.setObjectName("pushButtonEditPromote")
        self.pushButtonEditDemote = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButtonEditDemote.setGeometry(QtCore.QRect(20, 340, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonEditDemote.setFont(font)
        self.pushButtonEditDemote.setObjectName("pushButtonEditDemote")
        self.groupBoxPromote = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBoxPromote.setGeometry(QtCore.QRect(240, 60, 471, 331))
        self.groupBoxPromote.setTitle("")
        self.groupBoxPromote.setObjectName("groupBoxPromote")
        self.pushButtonHideEdit = QtWidgets.QPushButton(self.groupBoxPromote)
        self.pushButtonHideEdit.setGeometry(QtCore.QRect(410, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonHideEdit.setFont(font)
        self.pushButtonHideEdit.setObjectName("pushButtonHideEdit")
        self.lineEditPartyEdit = QtWidgets.QLineEdit(self.groupBoxPromote)
        self.lineEditPartyEdit.setGeometry(QtCore.QRect(20, 30, 371, 31))
        self.lineEditPartyEdit.setObjectName("lineEditPartyEdit")
        self.lineEditPositionEdit = QtWidgets.QLineEdit(self.groupBoxPromote)
        self.lineEditPositionEdit.setGeometry(QtCore.QRect(20, 80, 371, 31))
        self.lineEditPositionEdit.setObjectName("lineEditPositionEdit")
        self.textEditPlatform = QtWidgets.QTextEdit(self.groupBoxPromote)
        self.textEditPlatform.setGeometry(QtCore.QRect(20, 130, 371, 101))
        self.textEditPlatform.setObjectName("textEditPlatform")
        self.lineEditPathEdit = QtWidgets.QLineEdit(self.groupBoxPromote)
        self.lineEditPathEdit.setGeometry(QtCore.QRect(20, 250, 371, 31))
        self.lineEditPathEdit.setObjectName("lineEditPathEdit")
        self.pushButtonHideEdit_2 = QtWidgets.QPushButton(self.groupBoxPromote)
        self.pushButtonHideEdit_2.setGeometry(QtCore.QRect(150, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonHideEdit_2.setFont(font)
        self.pushButtonHideEdit_2.setObjectName("pushButtonHideEdit_2")
        self.lineEditSearchEdit.raise_()
        self.pushButtonSearchEdit.raise_()
        self.label_2.raise_()
        self.pushButtonEdit.raise_()
        self.lineEditNameEdit.raise_()
        self.lineEditStudentNumEdit.raise_()
        self.lineEditPasswordEdit.raise_()
        self.scrollAreaSumm.raise_()
        self.pushButtonEditPromote.raise_()
        self.pushButtonEditDemote.raise_()
        self.groupBoxPromote.raise_()
        self.scrollAreaEdit.setWidget(self.scrollAreaWidgetContents_4)
        self.pushButtonCreateUser.raise_()
        self.pushButtonDeleteUser.raise_()
        self.pushButtonEditUser.raise_()
        self.pushButtonStartElec.raise_()
        self.pushButtonEndElec.raise_()
        self.pushButtonSummary.raise_()
        self.scrollAreaCreateUser.raise_()
        self.pushButton.raise_()
        self.scrollAreaDelete.raise_()
        self.labelElectionStatus.raise_()
        self.scrollAreaSumm.raise_()
        self.scrollAreaEdit.raise_()

        projDirectory = self.projDirectory.replace("\\", "/")
        background = ("QWidget#Admin{background-image: url(\"" + projDirectory
                      + "/Resources/LogInBackground.jpg\"); background-position: center;}")
        Admin.setStyleSheet(background + open(projDirectory
                                              + "\Resources\Design.qss", 'r').read())
        Admin.setWindowIcon(QtGui.QIcon(projDirectory
                                        + "\Resources\MapuaIcon.png"))
        font.setPointSize(14)
        self.pushButtonCreateUser.setFont(font)
        self.pushButtonDeleteUser.setFont(font)
        self.pushButtonEditUser.setFont(font)
        self.pushButtonStartElec.setFont(font)
        self.pushButtonEndElec.setFont(font)
        font.setPointSize(10)
        self.pushButtonSummary.setFont(font)
        font.setPointSize(16)
        self.lineEditPositionEdit.setFont(font)
        self.lineEditPartyEdit.setFont(font)
        self.lineEditPathEdit.setFont(font)
        self.lineEditNameAdmin.setFont(font)
        self.lineEditPassAdmin.setFont(font)
        self.lineEditReenterPassAdmin.setFont(font)
        self.lineEditProgram.setFont(font)
        self.lineEditName.setFont(font)
        self.lineEditStudentNum.setFont(font)
        self.lineEditPass.setFont(font)
        self.lineEditReenterPass.setFont(font)
        self.lineEditSearch.setFont(font)
        self.lineEditSearchEdit.setFont(font)
        self.lineEditNameEdit.setFont(font)
        self.lineEditStudentNumEdit.setFont(font)
        self.lineEditPasswordEdit.setFont(font)
        self.textEditPlatform.setStyleSheet("color: gray")
        self.lineEditPartyEdit.setStyleSheet("color: gray")
        self.lineEditPositionEdit.setStyleSheet("color: gray")
        self.lineEditPathEdit.setStyleSheet("color: gray")
        self.lineEditNameAdmin.setStyleSheet("color: gray")
        self.lineEditPassAdmin.setStyleSheet("color: gray")
        self.lineEditReenterPassAdmin.setStyleSheet("color: gray")
        self.lineEditProgram.setStyleSheet("color: gray")
        self.lineEditName.setStyleSheet("color: gray")
        self.lineEditStudentNum.setStyleSheet("color: gray")
        self.lineEditPass.setStyleSheet("color: gray")
        self.lineEditReenterPass.setStyleSheet("color: gray")
        self.lineEditSearch.setStyleSheet("color: gray")
        self.lineEditSearchEdit.setStyleSheet("color: gray")
        self.lineEditNameEdit.setStyleSheet("color: gray")
        self.lineEditStudentNumEdit.setStyleSheet("color: gray")
        self.lineEditPasswordEdit.setStyleSheet("color: gray")
        self.textEditPlatform.setPlaceholderText("Platform")
        self.lineEditPositionEdit.setPlaceholderText("Position")
        self.lineEditPartyEdit.setPlaceholderText("Party")
        self.lineEditPathEdit.setPlaceholderText("Picture Path")
        self.lineEditNameAdmin.setPlaceholderText("LastName, GivenName, MiddleName")
        self.lineEditPassAdmin.setPlaceholderText("Password")
        self.lineEditReenterPassAdmin.setPlaceholderText("Re-enter Password")
        self.lineEditProgram.setPlaceholderText("Program")
        self.lineEditName.setPlaceholderText("LastName, GivenName, MiddleName")
        self.lineEditStudentNum.setPlaceholderText("Student number")
        self.lineEditPass.setPlaceholderText("Password")
        self.lineEditReenterPass.setPlaceholderText("Re-enter password")
        self.lineEditSearch.setPlaceholderText("Student number")
        self.lineEditSearchEdit.setPlaceholderText("Student number")
        self.lineEditNameEdit.setPlaceholderText("LastName, GivenName, MiddleName")
        self.lineEditStudentNumEdit.setPlaceholderText("Student number")
        self.lineEditPasswordEdit.setPlaceholderText("Password")
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.hide()
        self.groupBoxAdmin.hide()
        self.groupBoxPromote.hide()
        font.setPointSize(20)
        self.comboBoxPosition.setFont(font)
        strPositions = ['PRESIDENT', 'INTERNAL VICE PRESIDENT', 'EXTERNAL VICE PRESIDENT', 'EXECUTIVE SECRETARY',
                        'SECRETARY OF FINANCE', 'SECRETARY OF AUDIT', 'SECRETARY OF LOGISTICS',
                        'SECRETARY OF SCHOLARSHIP AFFAIRS', 'SECRETARY OF INFORMATION AND CORRESPONDENCE',
                        'SECRETARY OF AMUSEMENT AND RECREATION', 'SECRETARY OF WELFARE AND DEVELOPMENT',
                        '4TH YEAR REPRESENTATIVE', '3RD YEAR REPRESENTATIVE', '2ND YEAR REPRESENTATIVE',
                        'GENERAL ENGINEERING REPRESENTATIVE', 'CSC REPRESENTATIVE', 'BUSINESS MANAGER']
        self.comboBoxPosition.addItems(strPositions)
        self.isUser = True

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)
        Admin.setTabOrder(self.pushButtonCreateUser, self.pushButtonDeleteUser)
        Admin.setTabOrder(self.pushButtonDeleteUser, self.pushButtonEditUser)
        Admin.setTabOrder(self.pushButtonEditUser, self.pushButtonStartElec)
        Admin.setTabOrder(self.pushButtonStartElec, self.pushButtonEndElec)
        Admin.setTabOrder(self.pushButtonEndElec, self.pushButtonSummary)
        Admin.setTabOrder(self.pushButtonSummary, self.scrollAreaCreateUser)
        Admin.setTabOrder(self.scrollAreaCreateUser, self.lineEditName)
        Admin.setTabOrder(self.lineEditName, self.lineEditStudentNum)
        Admin.setTabOrder(self.lineEditStudentNum, self.lineEditProgram)
        Admin.setTabOrder(self.lineEditProgram, self.lineEditPass)
        Admin.setTabOrder(self.lineEditPass, self.lineEditReenterPass)
        Admin.setTabOrder(self.lineEditReenterPass, self.pushButtonCreate)
        Admin.setTabOrder(self.pushButtonCreate, self.scrollAreaDelete)
        Admin.setTabOrder(self.scrollAreaDelete, self.pushButton)
        Admin.setTabOrder(self.pushButton, self.scrollAreaEdit)
        Admin.setTabOrder(self.scrollAreaEdit, self.lineEditSearchEdit)
        Admin.setTabOrder(self.lineEditSearchEdit, self.pushButtonSearchEdit)
        Admin.setTabOrder(self.pushButtonSearchEdit, self.pushButtonEdit)
        Admin.setTabOrder(self.pushButtonEdit, self.lineEditNameEdit)
        Admin.setTabOrder(self.lineEditNameEdit, self.lineEditStudentNumEdit)
        Admin.setTabOrder(self.lineEditStudentNumEdit, self.lineEditPasswordEdit)
        Admin.setTabOrder(self.lineEditPasswordEdit, self.comboBoxPosition)
        Admin.setTabOrder(self.comboBoxPosition, self.lineEditSearch)
        Admin.setTabOrder(self.lineEditSearch, self.pushButtonSearch)
        Admin.setTabOrder(self.pushButtonSearch, self.pushButtonDelete)
        Admin.setTabOrder(self.pushButtonDelete, self.scrollAreaSumm)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Mapua University"))
        self.pushButtonCreateUser.setText(_translate("Admin", "Create User"))
        self.pushButtonDeleteUser.setText(_translate("Admin", "Delete User"))
        self.pushButtonEditUser.setText(_translate("Admin", "Edit User"))
        self.pushButtonStartElec.setText(_translate("Admin", "Start Election"))
        self.pushButtonEndElec.setText(_translate("Admin", "End Election"))
        self.pushButtonSummary.setText(_translate("Admin", "See Summary of Votes"))
        self.pushButtonCreate.setText(_translate("Admin", "Create"))
        self.pushButtonUser.setText(_translate("Admin", "User"))
        self.pushButtonAdmin.setText(_translate("Admin", "Admin"))
        self.pushButton.setText(_translate("Admin", "Signout"))
        self.pushButtonSearch.setText(_translate("Admin", "Search"))
        self.labelDelProfile.setText(_translate("Admin",
                                                "<html><head/><body><p><span style=\" font-size:20pt;\">Name: </span></p><p><span style=\" font-size:20pt;\">Student Number: </span></p><p><span style=\" font-size:20pt;\">Email: </span></p></body></html>"))
        self.pushButtonDelete.setText(_translate("Admin", "Delete"))
        self.labelElectionStatus.setText(_translate("Admin",
                                                    "<html><head/><body><p><span style=\" font-size:26pt;\">Election on going</span></p></body></html>"))
        self.label.setText(_translate("Admin", "TextLabel"))
        self.label_3.setText(_translate("Admin", "<html><head/><body><p>Candidate 1</p><p>Vote:</p></body></html>"))
        self.label_4.setText(_translate("Admin", "TextLabel"))
        self.label_5.setText(_translate("Admin", "<html><head/><body><p>Candidate 2:</p><p>Vote:</p></body></html>"))
        self.pushButtonSearchEdit.setText(_translate("Admin", "Search"))
        self.label_2.setText(_translate("Admin",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">Name: </span></p><p><span style=\" font-size:10pt;\">Student Number: </span></p><p><span style=\" font-size:10pt;\">Password: </span></p></body></html>"))
        self.pushButtonEdit.setText(_translate("Admin", "Edit"))
        self.pushButtonEditPromote.setText(_translate("Admin", "Promote to Candidate"))
        self.pushButtonEditDemote.setText(_translate("Admin", "Demote to User"))
        self.pushButtonHideEdit.setText(_translate("Admin", "Hide"))
        self.textEditPlatform.setHtml(_translate("Admin",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        self.pushButtonHideEdit_2.setText(_translate("Admin", "Promote"))
        self.pushButtonCreateUser.clicked.connect(self.showCreateUser)
        self.pushButtonDeleteUser.clicked.connect(self.showDeleteUser)
        self.pushButtonEditUser.clicked.connect(self.showEditUser)
        self.pushButtonSummary.clicked.connect(self.showSummary)
        self.textEditPlatform.textChanged.connect(self.inputPlatform)
        self.lineEditPositionEdit.textChanged.connect(self.inputPosition)
        self.lineEditPartyEdit.textChanged.connect(self.inputPartyEdit)
        self.lineEditPathEdit.textChanged.connect(self.inputPathEdit)
        self.lineEditNameAdmin.textChanged.connect(self.inputNameAdmin)
        self.lineEditPassAdmin.textChanged.connect(self.inputPassAdmin)
        self.lineEditReenterPassAdmin.textChanged.connect(self.inputReenterPassAdmin)
        self.lineEditName.textChanged.connect(self.inputName)
        self.lineEditStudentNum.textChanged.connect(self.inputStudentNum)
        self.lineEditPass.textChanged.connect(self.inputPass)
        self.lineEditReenterPass.textChanged.connect(self.inputReenterPass)
        self.lineEditSearch.textChanged.connect(self.inputSearch)
        self.lineEditSearchEdit.textChanged.connect(self.inputSearchEdit)
        self.lineEditNameEdit.textChanged.connect(self.lineEditNameEditChanged)
        self.lineEditStudentNumEdit.textChanged.connect(self.lineEditStudentNumEditChanged)
        self.lineEditPasswordEdit.textChanged.connect(self.lineEditPasswordEditChanged)
        self.lineEditProgram.textChanged.connect(self.inputProgram)
        self.pushButtonCreate.clicked.connect(self.create)
        self.pushButtonStartElec.clicked.connect(self.startElec)
        self.pushButtonEndElec.clicked.connect(self.endElec)
        self.pushButtonDelete.clicked.connect(self.delete)
        self.pushButtonEdit.clicked.connect(self.edit)
        self.pushButtonSearch.clicked.connect(self.searchDelete)
        self.pushButtonSearchEdit.clicked.connect(self.searchEdit)
        self.pushButtonAdmin.clicked.connect(self.showAdmin)
        self.pushButtonUser.clicked.connect(self.showUser)
        self.pushButtonEditPromote.clicked.connect(self.showPromote)
        self.pushButtonEditDemote.clicked.connect(self.demote)
        self.pushButtonHideEdit.clicked.connect(self.hidePromote)
        self.pushButtonHideEdit_2.clicked.connect(self.promote)
        self.comboBoxPosition.currentIndexChanged.connect(self.position_selection_changed)

        #   check if an election is on going, set proper labels
        if (Election.GetExistingElectionStartDate() is None):
            self.labelElectionStatus.setText(_translate("Admin",
                                                        "<html><head/><body><p><span style=\" font-size:26pt;\">NO ELECTION STARTED YET</span></p></body></html>"))
        else:
            self.labelElectionStatus.setText(_translate("Admin", "<html><head/><body><p><span style=\" font-size:26pt;\">ELECTION ON GOING</span></p></body></html>"))
        
    def showCreateUser(self):
        self.scrollAreaCreateUser.show()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.hide()
    def showDeleteUser(self):
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.show()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.hide()
    def showEditUser(self):
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.show()
        self.scrollAreaSumm.hide()
    def showSummary(self):
        self.position_selection_changed(0)
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.show()
    def inputSearch(self):
        self.lineEditSearch.setStyleSheet("color: white")
        if self.lineEditSearch.text() == "":
            self.lineEditSearch.setStyleSheet("color: gray")
    def inputSearchEdit(self):
        self.lineEditSearchEdit.setStyleSheet("color: white")
        if self.lineEditSearchEdit.text() == "":
            self.lineEditSearchEdit.setStyleSheet("color: gray")
    def inputName(self):
        self.lineEditName.setStyleSheet("color: white")
        if self.lineEditName.text() == "":
            self.lineEditName.setStyleSheet("color: gray")
    def inputStudentNum(self):
        self.lineEditStudentNum.setStyleSheet("color: white")
        if self.lineEditStudentNum.text() == "":
            self.lineEditStudentNum.setStyleSheet("color: gray")
    def lineEditNameEditChanged(self):
        self.lineEditNameEdit.setStyleSheet("color: white")
        if self.lineEditNameEdit.text() == "":
            self.lineEditNameEdit.setStyleSheet("color: gray")
    def lineEditStudentNumEditChanged(self):
        self.lineEditStudentNumEdit.setStyleSheet("color: white")
        if self.lineEditStudentNumEdit.text() == "":
            self.lineEditStudentNumEdit.setStyleSheet("color: gray")
    def lineEditPasswordEditChanged(self):
        self.lineEditPasswordEdit.setStyleSheet("color: white")
        if self.lineEditPasswordEdit.text() == "":
            self.lineEditPasswordEdit.setStyleSheet("color: gray")

    def inputPass(self):
        self.lineEditPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPass.setStyleSheet("color: white")
        if self.lineEditPass.text() == "":
            self.lineEditPass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPass.setStyleSheet("color: gray")  
    def inputReenterPass(self):
        self.lineEditReenterPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditReenterPass.setStyleSheet("color: white")
        if self.lineEditReenterPass.text() == "":
            self.lineEditReenterPass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditReenterPass.setStyleSheet("color: gray")

    def showPromote(self):
        self.lineEditNameEdit.hide()
        self.lineEditPasswordEdit.hide()
        self.lineEditStudentNumEdit.hide()
        self.pushButtonEdit.hide()
        self.groupBoxPromote.show()

    def hidePromote(self):
        self.lineEditNameEdit.show()
        self.lineEditPasswordEdit.show()
        self.lineEditStudentNumEdit.show()
        self.pushButtonEdit.show()
        self.groupBoxPromote.hide()

    def inputNameAdmin(self):
        self.lineEditNameAdmin.setStyleSheet("color: white")
        if self.lineEditNameAdmin.text() == "":
            self.lineEditNameAdmin.setStyleSheet("color: gray")

    def inputPassAdmin(self):
        self.lineEditPassAdmin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassAdmin.setStyleSheet("color: white")
        if self.lineEditPassAdmin.text() == "":
            self.lineEditPassAdmin.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPassAdmin.setStyleSheet("color: gray")

    def inputReenterPassAdmin(self):
        self.lineEditReenterPassAdmin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditReenterPassAdmin.setStyleSheet("color: white")
        if self.lineEditReenterPassAdmin.text() == "":
            self.lineEditReenterPassAdmin.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditReenterPassAdmin.setStyleSheet("color: gray")

    def inputPlatform(self):
        self.textEditPlatform.setStyleSheet("color: white")
        if self.textEditPlatform.toPlainText() == "":
            self.textEditPlatform.setStyleSheet("color: gray")

    def inputPosition(self):
        self.lineEditPositionEdit.setStyleSheet("color: white")
        if self.lineEditPositionEdit.text() == "":
            self.lineEditPositionEdit.setStyleSheet("color: gray")

    def inputPartyEdit(self):
        self.lineEditPartyEdit.setStyleSheet("color: white")
        if self.lineEditPartyEdit.text() == "":
            self.lineEditPartyEdit.setStyleSheet("color: gray")

    def inputPathEdit(self):
        self.lineEditPathEdit.setStyleSheet("color: white")
        if self.lineEditPathEdit.text() == "":
            self.lineEditPathEdit.setStyleSheet("color: gray")

    def inputProgram(self):
        self.lineEditProgram.setStyleSheet("color: white")
        if self.lineEditProgram.text() == "":
            self.lineEditProgram.setStyleSheet("color: gray")

    def PassAdminInfo(self, admin: Admin):
        self.adminInterface = AdminInterface(admin)
        self.elecInteface = Election.init_with_null()

    """
    ADMIN FUNCTIONS    
    """

    def position_selection_changed(self, args):
        print('Summary of Votes: Selection Changed to ' + self.comboBoxPosition.itemText(args))
        #reshow all hidden controls
        self.label_3.show()
        self.label.show()
        self.label_5.show()
        self.label_4.show()

        parties = self.elecInteface.GetPartyList()
        #   display votes
        #   candidate 1
        candidate = parties[0].GetCandidate(Position(args))

        if candidate is not None:
            #   set name and number of votes
            fullName = candidate.GetLastName() + ', ' + candidate.GetFirstName()
            self.label_3.setText(
                """
                <html>
                    <head/>
                        <body>
                            <p>
                                """+ fullName +' from ' + candidate.GetPartyName() + """
                            </p>
                            <p>
                                """+ 'Vote Count: ' + str(self.elecInteface.GetVotesFor(candidate.GetUserId())) + """
                            </p>
                        </body>
                </html>
                """
            )

            #   set pic
            picPath = os.path.join(self.projDirectory, candidate.GetPicturePath())
            candidatePic = QtGui.QPixmap(picPath)
            scaledCandPic = candidatePic.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(scaledCandPic)

        else:
            self.label.show()
            self.label_3.hide()

        #   candidate 2
        candidate = parties[1].GetCandidate(Position(args))

        if candidate is not None:
            #   set name and number of votes
            fullName = candidate.GetLastName() + ', ' + candidate.GetFirstName()
            self.label_5.setText(
                """
                <html>
                    <head/>
                            <body>
                            <p>
                                """ + fullName + ' from ' + candidate.GetPartyName() + """
                                                </p>
                                                <p>
                                                    """ + 'Vote Count: ' + str(
                    self.elecInteface.GetVotesFor(candidate.GetUserId())) + """
                                                </p>
                                            </body>
                                    </html>
                                    """
            )

            #   set pic
            picPath = os.path.join(self.projDirectory, candidate.GetPicturePath())
            candidatePic = QtGui.QPixmap(picPath)
            scaledCandPic = candidatePic.scaled(self.label_4.size(), QtCore.Qt.KeepAspectRatio)
            self.label_4.setPixmap(scaledCandPic)

        else:
            self.label_4.hide()
            self.label_5.hide()

    #   DELETE EXISTING USER
    def delete(self):
        if not self.adminInterface.is_user_set():
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'No User Set',
                                            'Please find a User first.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return
        else:
            #   super admin can delete admins: its id is 0
            if self.adminInterface.GetUser().GetUserId() == 0:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Attempt to Delete Super Admin',
                                                'You cannot delete super admin.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return
            if self.adminInterface.is_user_admin() and\
                    not self.adminInterface.is_super_admin():
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Attempt to Delete Admin',
                                                'You do not have the required privilege to delete an admin.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return

            #   ask for confirmation of deletion since this is will permanently lose the data
            #   distinguish between Candidate and User
            response = None
            if (self.adminInterface.is_Candidate()):
                confirmMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'Delete User?',
                                                   'This is not reversible, are you sure you want to delete this user?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                confirmMsg.setInformativeText('This user has been detected to be also a candidate.')
                response = confirmMsg.exec()
            else:
                confirmMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'Delete User?',
                                                   'This is not reversible, are you sure you want to delete this user?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                response = confirmMsg.exec()
            if response == QtWidgets.QMessageBox.Yes:
                self.adminInterface.remove_user()
                self.adminInterface.reset_user()
                self.labelDelProfile.setText(
                    "<html><head/><body><p>"
                    "<span style=\" font-size:20pt;\">"
                    "Name: "
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Student Number: "
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Email: "
                    "</span>"
                    "</p>"
                    "</body>"
                    "</html>")
                successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'User Deleted',
                                                   'User successfully removed from database.',
                                                   QtWidgets.QMessageBox.Ok)
                successMsg.exec()

    #   EDIT EXISTING USER
    def edit(self):
        print('EDIT METHOD CALLED')
        self.adminInterface.reset_user()
        #   get user inputs
        fullName = self.lineEditNameEdit.text()
        studNum = self.lineEditStudentNumEdit.text()
        password = self.lineEditPasswordEdit.text()

        #   input formatting, also check for erroneous inputs
        #   fullName : input check and clear
        names = fullName.split(',')
        if len(names) != 3:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Full Name must follow format. Include commas to separate '
                                            'the three names.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return
        else:
            lastName = names[0].strip()
            firstName = names[1].strip()
            midName = names[2].strip()

        #   studNum : input check and clear
        if len(studNum.strip()) < 1 or len(studNum.strip()) > 10:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Student number must only be composed of numbers'
                                            ' and at most 10 digits.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return
        try:
            studNum = int(studNum)
        except ValueError:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Student number must only be composed of numbers'
                                            ' and at most 10 digits.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return

        #   password : input check and clear
        if not len(password) == 0 and not password.isalnum() and len(password) < 6:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Password must be composed of letters and numbers only, '
                                            'and at least 6 characters.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
        else:
            #   inputs verified, update User
            self.adminInterface.set_user_using_userId(studNum)
            modifiedUser = self.adminInterface.GetUser()

            if self.adminInterface.is_user_set():
                modifiedUser.SetName(firstName, midName, lastName)
                modifiedUser.SetPassword(password)
                self.adminInterface.set_updated_user(modifiedUser)
                self.adminInterface.update_user()
                successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'Success!',
                                                   'Successfully updated user in database.',
                                                   QtWidgets.QMessageBox.Ok)
                successMsg.exec()
            else:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'No Match Found',
                                                'Student ID entered does not exist, please enter'
                                                ' a valid one. Use the search feature to find one.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()

    #   CREATE THE NEW USER PROFILE
    def create(self):
        if self.isUser:
            print("CREATE THE NEW USER PROFILE")
            self.adminInterface.reset_user()
            #   get user inputs
            fullName = self.lineEditName.text()
            studNum = self.lineEditStudentNum.text()
            prog = self.lineEditProgram.text()
            password = self.lineEditPass.text()
            confirmPassword = self.lineEditReenterPass.text()

            #   input formatting, also check for erroneous inputs
            #   fullName : input check and clear
            names = fullName.split(',')
            if len(names) != 3:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Incorrect Input',
                                                'Full Name must follow format. Include commas to separate '
                                                'the three names.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return
            else:
                lastName = names[0].strip()
                firstName = names[1].strip()
                midName = names[2].strip()

            #   studNum : input check and clear
            if len(studNum.strip()) < 1 or len(studNum.strip()) > 10:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Incorrect Input',
                                                'Student number must only be composed of numbers'
                                                ' and at most 10 digits.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return
            try:
                studNum = int(studNum)
            except ValueError:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Incorrect Input',
                                                'Student number must only be composed of numbers'
                                                ' and at most 10 digits.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return

            #   program : input check and clear
            if len(prog) == 0:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Incorrect Input',
                                                'Program field must not be empty.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return

            #   password : input check and clear
            if not len(password) == 0 and not password.isalnum() and len(password) < 6:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Incorrect Input',
                                                'Password must be composed of letters and numbers only, '
                                                'and at least 6 characters.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
            else:
                if (password != confirmPassword):
                    failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                    'Incorrect Input',
                                                    'Password and confirm password do not match.',
                                                    QtWidgets.QMessageBox.Ok)
                    failMsg.exec()
                else:
                    #   inputs verified, create User
                    newUser = User(studNum, prog, firstName, midName, lastName, password)
                    self.adminInterface.set_new_user(newUser)
                    if self.adminInterface.is_user_set():
                        self.adminInterface.add_user_to_database()
                        successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                        'Success!',
                                                        'Successfully added new user to database.',
                                                        QtWidgets.QMessageBox.Ok)
                        successMsg.exec()
                    else:
                        failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                        'Duplicate Found',
                                                        'Student ID entered is already existing, please enter'
                                                        ' another.',
                                                        QtWidgets.QMessageBox.Ok)
                        failMsg.exec()

        else:
            print("CREATE THE NEW ADMIN PROFILE")
            self.adminInterface.reset_user()
            #   get user inputs
            fullName = self.lineEditNameAdmin.text()
            studNum = '10000' + str(self.adminInterface.get_admin_count() + 1)
            prog = 'ADMINISTRATOR'
            password = self.lineEditPassAdmin.text()
            confirmPassword = self.lineEditReenterPassAdmin.text()

            #   input formatting, also check for erroneous inputs
            #   fullName : input check and clear
            names = fullName.split(',')
            if len(names) != 3:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Incorrect Input',
                                                'Full Name must follow format. Include commas to separate '
                                                'the three names.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return
            else:
                lastName = names[0].strip()
                firstName = names[1].strip()
                midName = names[2].strip()

            #   password : input check and clear
            if not len(password) == 0 and not password.isalnum() and len(password) < 6:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Incorrect Input',
                                                'Password must be composed of letters and numbers only, '
                                                'and at least 6 characters.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
            else:
                if (password != confirmPassword):
                    failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                    'Incorrect Input',
                                                    'Password and confirm password do not match.',
                                                    QtWidgets.QMessageBox.Ok)
                    failMsg.exec()
                else:
                    #   inputs verified, create User
                    if password == '':
                        password = None
                    newUser = User(studNum, prog, firstName, midName, lastName, password)
                    self.adminInterface.set_new_user(newUser)
                    if self.adminInterface.is_user_set():
                        self.adminInterface.add_user_to_database()
                        successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                           'Success!',
                                                           'Successfully added new user to database.',
                                                           QtWidgets.QMessageBox.Ok)
                        successMsg.exec()
                    else:
                        failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                        'Duplicate Found',
                                                        'Student ID entered is already existing, please enter'
                                                        ' another.',
                                                        QtWidgets.QMessageBox.Ok)
                        failMsg.exec()

    #   SEARCH STUDENT NUMBER FROM DELETE
    def searchDelete(self):
        #   reset the current set user in AdminInterface first to prevent unexpected outputs
        self.adminInterface.reset_user()
        studId = self.lineEditSearch.text()
        try:
            studId = int(studId)
            self.adminInterface.set_user_using_userId(studId)

            if self.adminInterface.GetUser() is not None and self.adminInterface.is_User():
                #   display in labels the user information
                user = self.adminInterface.GetUser()
                self.labelDelProfile.setText(
                    "<html><head/><body><p>"
                    "<span style=\" font-size:20pt;\">"
                    "Name: " + user.GetLastName() + ", " + user.GetFirstName() + " " + user.GetMidName() +
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Student Number: " + (str)(user.GetUserId()) +
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Email: " + user.GetEmail() +
                    "</span>"
                    "</p>"
                    "</body>"
                    "</html>")
            else:
                notFoundMsg = QtWidgets.QMessageBox()
                notFoundMsg.setIcon(QtWidgets.QMessageBox.Information)
                notFoundMsg.setText('User not found.')
                notFoundMsg.setWindowTitle('Search User')
                notFoundMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                notFoundMsg.exec()

        except ValueError:
            errorMsg = QtWidgets.QMessageBox()
            errorMsg.setIcon(QtWidgets.QMessageBox.Information)
            errorMsg.setText('Incorrect student number inputted.')
            errorMsg.setWindowTitle('Input Error')
            errorMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            errorMsg.exec()

    #   SEARCH STUDENT NUMBER FROM EDIT
    def searchEdit(self):
        print('SEARCH EDIT CALLED')
        #   clear the candidate fields
        self.lineEditPartyEdit.clear()
        self.lineEditPositionEdit.clear()
        self.textEditPlatform.clear()
        self.lineEditPathEdit.clear()
        #   reset the current set user in AdminInterface first to prevent unexpected outputs
        self.adminInterface.reset_user()
        studId = self.lineEditSearchEdit.text()
        try:
            studId = int(studId)
            self.adminInterface.set_user_using_userId(studId)

            if self.adminInterface.is_user_set() and self.adminInterface.is_User():
                #   display in labels the user information
                user = self.adminInterface.GetUser()
                self.lineEditNameEdit.setText(user.GetLastName() + ', '
                                              + user.GetFirstName() +
                                              ', ' + user.GetMidName())
                self.lineEditStudentNumEdit.setText(str(user.GetUserId()))
                self.lineEditPasswordEdit.setText(user.GetPassword())

                #   check if candidate
                #   if so, set the party, position, platform, and picture path labels
                if self.adminInterface.is_Candidate():
                    candidate = self.adminInterface.GetUser()
                    self.lineEditPartyEdit.setText(candidate.GetPartyName())
                    self.lineEditPositionEdit.setText(str(candidate.GetPosition()).split('.')[1])
                    self.textEditPlatform.setText(candidate.GetPlatform())
                    self.lineEditPathEdit.setText(candidate.GetPicturePath())

            else:
                notFoundMsg = QtWidgets.QMessageBox()
                notFoundMsg.setIcon(QtWidgets.QMessageBox.Information)
                notFoundMsg.setText('User not found.')
                notFoundMsg.setWindowTitle('Search User')
                notFoundMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                notFoundMsg.exec()

        except ValueError:
            errorMsg = QtWidgets.QMessageBox()
            errorMsg.setIcon(QtWidgets.QMessageBox.Information)
            errorMsg.setText('Incorrect student number inputted.')
            errorMsg.setWindowTitle('Input Error')
            errorMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            errorMsg.exec()


    def startElec(self):
        self.labelElectionStatus.setText("<html><head/><body><p><span style=\" font-size:26pt;\">ELECTION ON GOING</span></p></body></html>")
        elecStartDate = datetime.now()
        electEndDate = elecStartDate + timedelta(days=self.election_duration)
        newElection = Election(elecStartDate, None)
        newElection.SetEndDate(electEndDate)

        newElection.StartElection()

    def endElec(self):
        self.labelElectionStatus.setText("<html><head/><body><p><span style=\" font-size:26pt;\">ELECTION ENDED</span></p></body></html>")
        Election.DropExistingElection()

    def promote(self):
        print("PROMOTE THE USER TO CANDIDATE")
        self.adminInterface.reset_user()
        #   get user inputs
        fullName = self.lineEditNameEdit.text().strip()
        studNum = self.lineEditStudentNumEdit.text().strip()
        password = self.lineEditPasswordEdit.text().strip()
        party = self.lineEditPartyEdit.text().strip()
        pos = self.lineEditPositionEdit.text().strip()
        platform = self.textEditPlatform.toPlainText().strip()
        picPath = self.lineEditPathEdit.text().strip()

        #   input formatting, also check for erroneous inputs
        #   fullName : input check and clear
        names = fullName.split(',')
        if len(names) != 3:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Full Name must follow format. Include commas to separate '
                                            'the three names.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return
        else:
            lastName = names[0].strip()
            firstName = names[1].strip()
            midName = names[2].strip()

        #   studNum : input check and clear
        if len(studNum.strip()) < 1 or len(studNum.strip()) > 10:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Student number must only be composed of numbers'
                                            ' and at most 10 digits.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return
        try:
            studNum = int(studNum)
        except ValueError:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Student number must only be composed of numbers'
                                            ' and at most 10 digits.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return

        #   password : input check and clear
        if not len(password) == 0 and not password.isalnum() and len(password) < 6:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Password must be composed of letters and numbers only, '
                                            'and at least 6 characters.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return

        #   party : input check and clear
        if len(party) == 0:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Party field must not be empty.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return

        #   pos : input check and clear
        try:
            pos = Position[pos.upper()]
        except KeyError:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Please be guided with the Position formatting below: ',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.setInformativeText("""
                                PRESIDENT,
                                VICE_PRESIDENT_INT,
                                VICE_PRESIDENT_EXT, 
                                SECRETARY_EXECUTIVE,
                                SECRETARY_FINANCE,  
                                SECRETARY_AUDIT,    
                                SECRETARY_LOGISTICS,
                                SECRETARY_SCHOLARSHIP,
                                SECRETARY_INFO_CORRESPONDENCE,
                                SECRETARY_AMUSEMENT_RECREATION,
                                SECRETARY_WELFARE_DEV,
                                REPRESENTATIVE_4TH_YEAR,
                                REPRESENTATIVE_3RD_YEAR,
                                REPRESENTATIVE_2ND_YEAR,
                                REPRESENTATIVE_GENERAL,
                                REPRESENTATIVE_CSC,
                                BUSINESS_MANAGER,
                                    """)
            failMsg.exec()
            return

        #   platform : auto clear, no need to check

        #   picPath : input check and clear
        if not os.path.isfile(os.path.join(os.getcwd(), picPath)):
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Path does not point to a valid file.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
        else:
            #   inputs verified, update Candidate
            self.adminInterface.set_user_using_userId(studNum)
            modifiedUser = self.adminInterface.GetUser()

            if self.adminInterface.is_user_set():
                modifiedUser.SetName(firstName, midName, lastName)
                modifiedUser.SetPassword(password)
                self.adminInterface.set_updated_user(modifiedUser)
                self.adminInterface.update_user()

                #   check if admin, admin cannot be a candidate
                if self.adminInterface.is_Admin():
                    failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                    'Illegal Promotion',
                                                    'Cannot promote an admin to candidate. Only users may become'
                                                    ' candidates.',
                                                    QtWidgets.QMessageBox.Ok)
                    failMsg.exec()
                    return
                #   check if already a candidate
                #   update candidate if so
                if self.adminInterface.is_Candidate():
                    modifiedCandidate = self.adminInterface.GetUser()
                    modifiedCandidate.SetPartyName(party)
                    modifiedCandidate.SetPosition(pos)
                    if platform != '':
                        modifiedCandidate.SetPlatform(platform)
                    modifiedCandidate.SetPicturePath(picPath)

                    #   check for conflicts
                    election = Election.init_with_null()
                    if any(party.GetPartyName() == modifiedCandidate.GetPartyName() and\
                           party.GetCandidate(pos) is not None\
                           for party in election.GetPartyList()):
                        failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                        'Conflicting Candidate',
                                                        'Cannot proceed with edit, candidate has a conflict '
                                                        'with one of the candidates'
                                                        ' in the database.',
                                                        QtWidgets.QMessageBox.Ok)
                        failMsg.exec()
                        return
                    else:
                        self.adminInterface.set_updated_user(modifiedCandidate)
                        self.adminInterface.update_user()
                        successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                           'Success!',
                                                           'Successfully updated candidate in database.',
                                                           QtWidgets.QMessageBox.Ok)
                        successMsg.exec()

                #   if not a candidate yet, check for conflicts then write to database
                else:
                    newCandidate = Candidate(modifiedUser.GetUserId(), modifiedUser.GetProgram(),
                                             modifiedUser.GetFirstName(), modifiedUser.GetMidName(),
                                             modifiedUser.GetLastName(), modifiedUser.GetPassword(), pos, party)
                    if platform != '':
                        newCandidate.SetPlatform(platform)
                    newCandidate.SetPicturePath(picPath)

                    #   check for conflicts
                    election = Election.init_with_null()
                    if any(party.GetPartyName() == newCandidate.GetPartyName() and \
                           party.GetCandidate(pos) is not None \
                           for party in election.GetPartyList()):
                        failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                        'Conflicting Candidate',
                                                        'Cannot proceed with edit, candidate has a conflict '
                                                        'with one of the candidates'
                                                        ' in the database.',
                                                        QtWidgets.QMessageBox.Ok)
                        failMsg.exec()
                        return
                    else:
                        #   clear voter tickets
                        self.adminInterface.is_Voter()
                        self.adminInterface.remove_user()
                        self.adminInterface.set_updated_user(newCandidate)
                        self.adminInterface.add_user_to_database()
                        self.adminInterface.update_user()
                        successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                           'Success!',
                                                           'Successfully promoted User to Candidate.',
                                                           QtWidgets.QMessageBox.Ok)
                        successMsg.exec()

                successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'Success!',
                                                   'Successfully updated user in database.',
                                                   QtWidgets.QMessageBox.Ok)
                successMsg.exec()
            else:
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'No Match Found',
                                                'Student ID entered does not exist, please enter'
                                                ' a valid one. Use the search feature to find one.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()


    def demote(self):
        print("DEMOTE THE CANDIDATE TO USER")
        #   clear currently set user just to be on the safe side
        self.adminInterface.reset_user()

        #   we only need one thing: the student id
        studNum = self.lineEditStudentNumEdit.text().strip()

        #   input formatting, also check for erroneous inputs

        #   studNum : input check and clear
        if len(studNum.strip()) < 1 or len(studNum.strip()) > 10:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Student number must only be composed of numbers'
                                            ' and at most 10 digits.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return
        try:
            studNum = int(studNum)
        except ValueError:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'Incorrect Input',
                                            'Student number must only be composed of numbers'
                                            ' and at most 10 digits.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()
            return

        self.adminInterface.set_user_using_userId(studNum)

        #   check if valid user id
        if self.adminInterface.is_user_set():
            #   check if admin, can't do anything with admin
            if self.adminInterface.is_Admin():
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                'Illegal Demotion',
                                                'Cannot demote an admin to candidate. Only users may become'
                                                ' candidates.',
                                                QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                return
            else:
                #   check if user is not a candidate, can't demote someone who isn't a candidate now can you?
                if self.adminInterface.is_Candidate():
                    demotedCandidate = self.adminInterface.GetUser()
                    self.adminInterface.remove_user()
                    self.adminInterface.set_new_user(User.morph_child_to_base(demotedCandidate))
                    self.adminInterface.add_user_to_database()

                    successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                       'Success!',
                                                       'Successfully demoted candidate to user.',
                                                       QtWidgets.QMessageBox.Ok)
                    successMsg.exec()
                else:
                    failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                    'Not a Candidate',
                                                    'Cannot demote user, user is not a candidate.',
                                                    QtWidgets.QMessageBox.Ok)
                    failMsg.exec()

        else:
            failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                            'No Match Found',
                                            'Student ID entered does not exist, please enter'
                                            ' a valid one. Use the search feature to find one.',
                                            QtWidgets.QMessageBox.Ok)
            failMsg.exec()

    def showAdmin(self):
        self.isUser = False
        self.groupBoxAdmin.show()
        self.groupBoxUser.hide()

    def showUser(self):
        self.isUser = True
        self.groupBoxAdmin.hide()
        self.groupBoxUser.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())