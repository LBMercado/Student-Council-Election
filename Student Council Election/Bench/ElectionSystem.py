# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ElectionSystem.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StudentElection(object):
    def setupUi(self, StudentElection):
        StudentElection.setObjectName("StudentElection")
        StudentElection.resize(526, 392)
        self.pushButtonNext = QtWidgets.QPushButton(StudentElection)
        self.pushButtonNext.setGeometry(QtCore.QRect(474, 0, 51, 391))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonPrev = QtWidgets.QPushButton(StudentElection)
        self.pushButtonPrev.setGeometry(QtCore.QRect(0, 0, 51, 391))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.label = QtWidgets.QLabel(StudentElection)
        self.label.setGeometry(QtCore.QRect(230, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(StudentElection)
        self.radioButton.setGeometry(QtCore.QRect(70, 80, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(StudentElection)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 220, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(StudentElection)
        self.pushButton.setGeometry(QtCore.QRect(150, 350, 241, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(StudentElection)
        QtCore.QMetaObject.connectSlotsByName(StudentElection)

    def retranslateUi(self, StudentElection):
        _translate = QtCore.QCoreApplication.translate
        StudentElection.setWindowTitle(_translate("StudentElection", "Mapua University"))
        self.pushButtonNext.setText(_translate("StudentElection", "Next"))
        self.pushButtonPrev.setText(_translate("StudentElection", "Prev"))
        self.label.setText(_translate("StudentElection", "Position"))
        self.radioButton.setText(_translate("StudentElection", "Name: "))
        self.radioButton_2.setText(_translate("StudentElection", "Name:"))
        self.pushButton.setText(_translate("StudentElection", "Submit"))

