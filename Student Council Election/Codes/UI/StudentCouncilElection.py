# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lauren\Desktop\SoftEng\UI\StudentCouncilElection.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from BusinessLogic.Election import Election
from BusinessLogic.Position import Position
from BusinessLogic.UserInterface import UserInterface

class Ui_StudentCouncilElection(object):
    def setupUi(self, StudentCouncilElection):
        self.fullName = "LastName, GivenName MI"
        self.email = "someone@mymail.mapua.edu.ph"
        self.projDirectory = os.getcwd()
        StudentCouncilElection.setObjectName("StudentCouncilElection")
        StudentCouncilElection.resize(1200, 600)
        self.listWidget = QtWidgets.QListWidget(StudentCouncilElection)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 120, 401))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButtonSubmit = QtWidgets.QPushButton(StudentCouncilElection)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(510, 520, 291, 51))
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        self.pushButtonPrev = QtWidgets.QPushButton(StudentCouncilElection)
        self.pushButtonPrev.setGeometry(QtCore.QRect(130, 80, 61, 401))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.pushButtonNext = QtWidgets.QPushButton(StudentCouncilElection)
        self.pushButtonNext.setGeometry(QtCore.QRect(1120, 80, 61, 401))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.labelProfile = QtWidgets.QLabel(StudentCouncilElection)
        self.labelProfile.setGeometry(QtCore.QRect(90, 10, 331, 51))
        self.labelProfile.setScaledContents(False)
        self.labelProfile.setWordWrap(True)
        self.labelProfile.setObjectName("labelProfile")
        self.pushButtonSignout = QtWidgets.QPushButton(StudentCouncilElection)
        self.pushButtonSignout.setGeometry(QtCore.QRect(1130, 10, 51, 51))
        self.pushButtonSignout.setObjectName("pushButtonSignout")
        self.pushButtonChangePass = QtWidgets.QPushButton(StudentCouncilElection)
        self.pushButtonChangePass.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.pushButtonChangePass.setObjectName("pushButtonChangePass")
        self.scrollArea = QtWidgets.QScrollArea(StudentCouncilElection)
        self.scrollArea.setGeometry(QtCore.QRect(190, 80, 931, 401))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -43, 912, 452))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.labelPosition = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelPosition.setFont(font)
        self.labelPosition.setObjectName("labelPosition")
        self.horizontalLayout.addWidget(self.labelPosition)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.checkBoxCandidate1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxCandidate1.setFont(font)
        self.checkBoxCandidate1.setObjectName("checkBoxCandidate1")
        self.verticalLayout_5.addWidget(self.checkBoxCandidate1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPic1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPic1.sizePolicy().hasHeightForWidth())
        self.labelPic1.setSizePolicy(sizePolicy)
        self.labelPic1.setMaximumSize(QtCore.QSize(120, 120))
        self.labelPic1.setObjectName("labelPic1")
        self.verticalLayout.addWidget(self.labelPic1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.labelD1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelD1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelD1.setWordWrap(True)
        self.labelD1.setObjectName("labelD1")
        self.horizontalLayout_2.addWidget(self.labelD1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.checkBoxCandidate2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxCandidate2.setFont(font)
        self.checkBoxCandidate2.setObjectName("checkBoxCandidate2")
        self.verticalLayout_5.addWidget(self.checkBoxCandidate2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelPic2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPic2.sizePolicy().hasHeightForWidth())
        self.labelPic2.setSizePolicy(sizePolicy)
        self.labelPic2.setMaximumSize(QtCore.QSize(120, 120))
        self.labelPic2.setObjectName("labelPic2")
        self.verticalLayout_2.addWidget(self.labelPic2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.labelD2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelD2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelD2.setWordWrap(True)
        self.labelD2.setObjectName("labelD2")
        self.horizontalLayout_3.addWidget(self.labelD2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.checkBoxCandidate3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxCandidate3.setFont(font)
        self.checkBoxCandidate3.setObjectName("checkBoxCandidate3")
        self.verticalLayout_5.addWidget(self.checkBoxCandidate3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelPic3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPic3.sizePolicy().hasHeightForWidth())
        self.labelPic3.setSizePolicy(sizePolicy)
        self.labelPic3.setMaximumSize(QtCore.QSize(120, 120))
        self.labelPic3.setObjectName("labelPic3")
        self.verticalLayout_3.addWidget(self.labelPic3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.labelD3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelD3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelD3.setWordWrap(True)
        self.labelD3.setObjectName("labelD3")
        self.horizontalLayout_4.addWidget(self.labelD3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.checkBoxCandidate4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxCandidate4.setFont(font)
        font.setPointSize(15)
        self.pushButtonSubmit.setFont(font)
        font.setPointSize(70)
        self.pushButtonNext.setFont(font)
        self.pushButtonPrev.setFont(font)
        self.checkBoxCandidate4.setObjectName("checkBoxCandidate4")
        self.verticalLayout_5.addWidget(self.checkBoxCandidate4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelPic4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPic4.sizePolicy().hasHeightForWidth())
        self.labelPic4.setSizePolicy(sizePolicy)
        self.labelPic4.setMaximumSize(QtCore.QSize(120, 120))
        self.labelPic4.setObjectName("labelPic4")
        self.verticalLayout_4.addWidget(self.labelPic4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.labelD4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelD4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelD4.setWordWrap(True)
        self.labelD4.setObjectName("labelD4")
        self.horizontalLayout_5.addWidget(self.labelD4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.labelD3.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButtonPrev.setEnabled(False)
        font.setPointSize(15)
        self.labelProfile.setFont(font)
        self.index = 0
        print(os.getcwd())
        projDirectory = self.projDirectory.replace("\\", "/")
        background = ("QWidget#StudentCouncilElection{background-image: url(\"" + projDirectory
                            +"/Resources/LogInBackground.jpg\"); background-position: center;}")
        StudentCouncilElection.setStyleSheet(background + open(projDirectory + "\Resources\Design.qss",'r').read())
        StudentCouncilElection.setWindowIcon(QtGui.QIcon(projDirectory + "\Resources\MapuaIcon.png"))
        pic = QtGui.QPixmap(projDirectory + "\Resources\MapuaLogo.png")
        self.labelPic1.setPixmap(pic)
        self.retranslateUi(StudentCouncilElection)
        QtCore.QMetaObject.connectSlotsByName(StudentCouncilElection)
        self.rdBtnGrp = Qt.QButtonGroup()
        self.rdBtnGrp.addButton(self.checkBoxCandidate1)
        self.rdBtnGrp.addButton(self.checkBoxCandidate2)
        self.rdBtnGrp.addButton(self.checkBoxCandidate3)
        self.rdBtnGrp.addButton(self.checkBoxCandidate4)

    def retranslateUi(self, StudentCouncilElection):
        _translate = QtCore.QCoreApplication.translate
        StudentCouncilElection.setWindowTitle(_translate("StudentCouncilElection", "Mapua University"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("StudentCouncilElection", "President"))
        item = self.listWidget.item(1)
        item.setText(_translate("StudentCouncilElection", "Vice President"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButtonSubmit.setText(_translate("StudentCouncilElection", "Submit Vote"))
        self.pushButtonPrev.setText(_translate("StudentCouncilElection", "<"))
        self.pushButtonNext.setText(_translate("StudentCouncilElection", ">"))
        self.labelProfile.setText(_translate("StudentCouncilElection", "<html><head/><body><p><span style=\" font-size:10pt;\">"+ self.fullName
                 +"</span></p><p><span style=\" font-size:10pt;\">" + self.email + "</span></p></body></html>"))
        self.pushButtonSignout.setText(_translate("StudentCouncilElection", "Sign out"))
        self.pushButtonChangePass.setText(_translate("StudentCouncilElection", "Change \n"
"Password"))
        self.labelPosition.setText(_translate("StudentCouncilElection", "PRESIDENT"))
        self.checkBoxCandidate1.setText(_translate("StudentCouncilElection", "Candidate 1"))
        self.labelD1.setText(_translate("StudentCouncilElection", "asjfhakhsfkahkj\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nasjda"))
        self.checkBoxCandidate2.setText(_translate("StudentCouncilElection", "Candidate 2"))
        self.labelPic2.setText(_translate("StudentCouncilElection", "Pic2"))
        self.labelD2.setText(_translate("StudentCouncilElection", "Description2"))
        self.checkBoxCandidate3.setText(_translate("StudentCouncilElection", "Candidate 3"))
        self.labelPic3.setText(_translate("StudentCouncilElection", "Pic3"))
        self.labelD3.setText(_translate("StudentCouncilElection", "Description3"))
        self.checkBoxCandidate4.setText(_translate("StudentCouncilElection", "Candidate 4"))
        self.labelPic4.setText(_translate("StudentCouncilElection", "Pic4"))
        self.labelD4.setText(_translate("StudentCouncilElection", "Description4"))
        self.pushButtonNext.clicked.connect(self.nextPos)
        self.pushButtonPrev.clicked.connect(self.prevPos)
        self.pushButtonChangePass.clicked.connect(self.ChangePassword)
        self.checkBoxCandidate1.clicked.connect(self.VoteForCandidate1)
        self.checkBoxCandidate2.clicked.connect(self.VoteForCandidate2)
        self.pushButtonSubmit.clicked.connect(self.FinalizeVotes)

    def nextPos(self):
        self.index += 1
        if self.index == 0:
            self.labelPosition.setText("PRESIDENT")
            self.load_election_interface(Position.PRESIDENT)
        elif self.index == 1:
            self.pushButtonPrev.setEnabled(True)
            self.labelPosition.setText("INTERNAL VICE PRESIDENT")
            self.load_election_interface(Position.VICE_PRESIDENT_INT)
        elif self.index == 2:
            self.labelPosition.setText("EXTERNAL VICE PRESIDENT")
            self.load_election_interface(Position.VICE_PRESIDENT_EXT)
        elif self.index == 3:
            self.labelPosition.setText("EXECUTIVE SECRETARY")
            self.load_election_interface(Position.SECRETARY_EXECUTIVE)
        elif self.index == 4:
            self.labelPosition.setText("SECRETARY OF FINANCE")
            self.load_election_interface(Position.SECRETARY_FINANCE)
        elif self.index == 5:
            self.labelPosition.setText("SECRETARY OF AUDIT")
            self.load_election_interface(Position.SECRETARY_AUDIT)
        elif self.index == 6:
            self.labelPosition.setText("SECRETARY OF LOGISTICS")
            self.load_election_interface(Position.SECRETARY_LOGISTICS)
        elif self.index == 7:
            self.labelPosition.setText("SECRETARY OF SCHOLARSHIP AFFAIRS")
            self.load_election_interface(Position.SECRETARY_SCHOLARSHIP)
        elif self.index == 8:
            self.labelPosition.setText("SECRETARY OF INFORMATION AND CORRESPONDENCE")
            self.load_election_interface(Position.SECRETARY_INFO_CORRESPONDENCE)
        elif self.index == 9:
            self.labelPosition.setText("SECRETARY OF AMUSEMENT AND RECREATION")
            self.load_election_interface(Position.SECRETARY_AMUSEMENT_RECREATION)
        elif self.index == 10:
            self.labelPosition.setText("SECRETARY OF WELFARE AND DEVELOPMENT")
            self.load_election_interface(Position.SECRETARY_WELFARE_DEV)
        elif self.index == 11:
            self.labelPosition.setText("4TH YEAR REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_4TH_YEAR)
        elif self.index == 12:
            self.labelPosition.setText("3RD YEAR REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_3RD_YEAR)
        elif self.index == 13:
            self.labelPosition.setText("2ND YEAR REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_2ND_YEAR)
        elif self.index == 14:
            self.labelPosition.setText("GENERAL ENGINEERING REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_GENERAL)
        elif self.index == 15:
            self.labelPosition.setText("CSC REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_CSC)
        elif self.index == 16:
            self.pushButtonNext.setEnabled(False)
            self.labelPosition.setText("BUSINESS MANAGER")
            self.load_election_interface(Position.BUSINESS_MANAGER)

    def prevPos(self):
        self.index -= 1

        if self.index == 0:
            self.pushButtonPrev.setEnabled(False)
            self.labelPosition.setText("PRESIDENT")
            self.load_election_interface(Position.PRESIDENT)
        elif self.index == 1:
            self.labelPosition.setText("INTERNAL VICE PRESIDENT")
            self.load_election_interface(Position.VICE_PRESIDENT_INT)
        elif self.index == 2:
            self.labelPosition.setText("EXTERNAL VICE PRESIDENT")
            self.load_election_interface(Position.VICE_PRESIDENT_EXT)
        elif self.index == 3:
            self.labelPosition.setText("EXECUTIVE SECRETARY")
            self.load_election_interface(Position.SECRETARY_EXECUTIVE)
        elif self.index == 4:
            self.labelPosition.setText("SECRETARY OF FINANCE")
            self.load_election_interface(Position.SECRETARY_FINANCE)
        elif self.index == 5:
            self.labelPosition.setText("SECRETARY OF AUDIT")
            self.load_election_interface(Position.SECRETARY_AUDIT)
        elif self.index == 6:
            self.labelPosition.setText("SECRETARY OF LOGISTICS")
            self.load_election_interface(Position.SECRETARY_LOGISTICS)
        elif self.index == 7:
            self.labelPosition.setText("SECRETARY OF SCHOLARSHIP AFFAIRS")
            self.load_election_interface(Position.SECRETARY_SCHOLARSHIP)
        elif self.index == 8:
            self.labelPosition.setText("SECRETARY OF INFORMATION AND CORRESPONDENCE")
            self.load_election_interface(Position.SECRETARY_INFO_CORRESPONDENCE)
        elif self.index == 9:
            self.labelPosition.setText("SECRETARY OF AMUSEMENT AND RECREATION")
            self.load_election_interface(Position.SECRETARY_AMUSEMENT_RECREATION)
        elif self.index == 10:
            self.labelPosition.setText("SECRETARY OF WELFARE AND DEVELOPMENT")
            self.load_election_interface(Position.SECRETARY_WELFARE_DEV)
        elif self.index == 11:
            self.labelPosition.setText("4TH YEAR REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_4TH_YEAR)
        elif self.index == 12:
            self.labelPosition.setText("3RD YEAR REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_3RD_YEAR)
        elif self.index == 13:
            self.labelPosition.setText("2ND YEAR REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_2ND_YEAR)
        elif self.index == 14:
            self.labelPosition.setText("GENERAL ENGINEERING REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_GENERAL)
        elif self.index == 15:
            self.pushButtonNext.setEnabled(True)
            self.labelPosition.setText("CSC REPRESENTATIVE")
            self.load_election_interface(Position.REPRESENTATIVE_CSC)
        elif self.index == 16:
            self.labelPosition.setText("BUSINESS MANAGER")
            self.load_election_interface(Position.BUSINESS_MANAGER)

    def setProfile(self, fullName, email):
        self.labelProfile.setText(fullName + "\n" + email)

    def pass_user_interface(self, userInterface: UserInterface):
        self.userInterface = userInterface
        #   set user as a voter
        self.userInterface.is_Voter()
        self.userVoter = self.userInterface.GetUser()

    def pass_election_interface(self, electionInt: Election):
        self.electionInterface = electionInt
        self.index = 0

        strPositions = ['PRESIDENT', 'INTERNAL VICE PRESIDENT', 'EXTERNAL VICE PRESIDENT', 'EXECUTIVE SECRETARY',
                        'SECRETARY OF FINANCE', 'SECRETARY OF AUDIT', 'SECRETARY OF LOGISTICS',
                        'SECRETARY OF SCHOLARSHIP AFFAIRS', 'SECRETARY OF INFORMATION AND CORRESPONDENCE',
                        'SECRETARY OF AMUSEMENT AND RECREATION', 'SECRETARY OF WELFARE AND DEVELOPMENT',
                        '4TH YEAR REPRESENTATIVE', '3RD YEAR REPRESENTATIVE', '2ND YEAR REPRESENTATIVE',
                        'GENERAL ENGINEERING REPRESENTATIVE', 'CSC REPRESENTATIVE', 'BUSINESS MANAGER']
        self.listWidget.clear()
        self.listWidget.addItems(strPositions)

        voteDict = self.userVoter.GetVoteTicket().GetVoteTicket()
        index = 0
        for vote in voteDict.keys():
            if voteDict[vote] is not None:
                self.listWidget.item(index).setForeground(Qt.QBrush(QtCore.Qt.green))
            index += 1

        self.load_election_interface(Position.PRESIDENT)

    def load_election_interface(self, pos: Position):
        #   president displayed at init
        #   assume two parties
        parties = self.electionInterface.GetPartyList()

        #   uncheck all radio buttons
        self.rdBtnGrp.setExclusive(False)
        self.checkBoxCandidate1.setChecked(False)
        self.checkBoxCandidate2.setChecked(False)
        self.rdBtnGrp.setExclusive(True)
        #   party 1
        candidate = parties[0].GetCandidate(pos)
        if candidate is not None:
            #   show controls
            self.checkBoxCandidate1.show()
            self.labelD1.show()
            self.labelPic1.show()
            if len(candidate.GetMidName()) > 0:
                self.checkBoxCandidate1.setText(candidate.GetFirstName() + ' ' +
                                                candidate.GetMidName()[0] + '. ' +
                                                candidate.GetLastName())
            else:
                self.checkBoxCandidate1.setText(candidate.GetFirstName()
                                                + ' ' +
                                                candidate.GetLastName())
            #   party 1 : set picture
            print(self.projDirectory + candidate.GetPicturePath())
            picPath = os.path.join(self.projDirectory, candidate.GetPicturePath())
            candidatePic = QtGui.QPixmap(picPath)
            scaledCandPic = candidatePic.scaled(self.labelPic1.size(), QtCore.Qt.KeepAspectRatio)
            self.labelPic1.setPixmap(scaledCandPic)

            #   party 1 : set platform
            self.labelD1.setText(candidate.GetPlatform())

            #   check if this is voted by user
            user_vote = self.userVoter.GetVoteTicket().GetVoteFromPosition(pos)
            if user_vote is not None or\
                user_vote == candidate.GetUserId():
                #   if so, set this radio button
                self.checkBoxCandidate1.setChecked(True)
                self.listWidget.item(self.index).setForeground(Qt.QBrush(QtCore.Qt.green))

        else:
            #   hide controls
            self.checkBoxCandidate1.hide()
            self.labelD1.hide()
            self.labelPic1.hide()

        #   party 2
        candidate = parties[1].GetCandidate(pos)
        if candidate is not None:
            #   show controls
            self.checkBoxCandidate2.show()
            self.labelD2.show()
            self.labelPic2.show()

            if len(candidate.GetMidName()) > 0:
                self.checkBoxCandidate2.setText(candidate.GetFirstName() + ' ' +
                                                candidate.GetMidName()[0] + '. ' +
                                                candidate.GetLastName())
            else:
                self.checkBoxCandidate2.setText(candidate.GetFirstName()
                                                + ' ' +
                                                candidate.GetLastName())
            #   party 2 : set picture
            picPath = os.path.join(self.projDirectory, candidate.GetPicturePath())
            candidatePic = QtGui.QPixmap(picPath)
            scaledCandPic = candidatePic.scaled(self.labelPic1.size(), QtCore.Qt.KeepAspectRatio)
            self.labelPic2.setPixmap(scaledCandPic)

            #   party 2 : set platform
            self.labelD2.setText(candidate.GetPlatform())

            #   check if this is voted by user
            user_vote = self.userVoter.GetVoteTicket().GetVoteFromPosition(pos)
            if user_vote is not None or \
                    user_vote == candidate.GetUserId():
                #   if so, set this radio button
                self.checkBoxCandidate1.setChecked(True)
                self.listWidget.item(self.index).setForeground(Qt.QBrush(QtCore.Qt.green))
        else:
            self.checkBoxCandidate2.hide()
            self.labelD2.hide()
            self.labelPic2.hide()

        #   hide other labels/controls
        self.checkBoxCandidate3.hide()
        self.labelD3.hide()
        self.labelPic3.hide()
        self.checkBoxCandidate4.hide()
        self.labelD4.hide()
        self.labelPic4.hide()

    def ChangePassword(self):
        #   ask for old password then set new one
        inputDialog = QtWidgets.QInputDialog()
        hasEnteredWrongPassword = True
        while hasEnteredWrongPassword:
            oldPassword, okPressed = QtWidgets.QInputDialog.getText(inputDialog,
                                                                  'Reset Password',
                                                                  'Enter your old password: ',
                                                                  QtWidgets.QLineEdit.Password,
                                                                  '')
            if okPressed and oldPassword == self.userInterface.GetUser().GetPassword():
                hasEnteredWrongPassword = False
            elif not okPressed:
                return

        newPassword, okPressed = QtWidgets.QInputDialog.getText(inputDialog,
                                                                'Reset Password',
                                                                'Enter your new password: ',
                                                                QtWidgets.QLineEdit.Password,
                                                                '')
        if okPressed:
            self.userInterface.UpdateUserPassword(newPassword)

    def VoteForCandidate1(self):
        self.userVoter.VoteFor(self.electionInterface.GetPartyList()[0].GetCandidate(Position(self.index)).GetUserId(),
                               Position(self.index))
        self.listWidget.item(self.index).setForeground(Qt.QBrush(QtCore.Qt.green))
    def VoteForCandidate2(self):
        self.userVoter.VoteFor(self.electionInterface.GetPartyList()[1].GetCandidate(Position(self.index)).GetUserId(),
                               Position(self.index))
        self.listWidget.item(self.index).setForeground(Qt.QBrush(QtCore.Qt.green))

    def FinalizeVotes(self):
        self.electionInterface.UpdateVoter(self.userVoter)
        msg = QtWidgets.QMessageBox()
        successMsg = QtWidgets.QMessageBox()
        successMsg.setIcon(QtWidgets.QMessageBox.Information)
        successMsg.setText('Your vote has been submitted. Thank you for participating!')
        successMsg.setWindowTitle('Student Council Elections')
        successMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        successMsg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentCouncilElection = QtWidgets.QWidget()
    ui = Ui_StudentCouncilElection()
    ui.setupUi(StudentCouncilElection)
    StudentCouncilElection.show()
    sys.exit(app.exec_())
