#!/usr/bin/env python

#import modules
from NameToEmail import NameToEmail

class User:
    def __init__(self, userId, program, firstName, middleName, lastName, password = None):
        self.userId = userId
        self.program = program
        self.firstName = firstName.lower()
        self.middleName = middleName.lower()
        self.lastName = lastName.lower()

        #If no supplied password, default password is userId
        if password is not None:
            self.password = userId
        else:
            self.password = password

        # assume first name is separated by spaces, split into a list
        firstNameList = self.firstName.split()
        # auto-generate an email address based on firstName, middleName, and lastName
        emailConverter = NameToEmail(firstNameList, self.middleName, self.lastName)
        emailConverter.ConvertNameToEmail()
        self.email = emailConverter.GetEmail()

    def GetUserId(self):
        return self.userId

    def SetProgram(self, program):
        self.program = program

    def GetProgram(self):
        return self.program

    def GetFirstName(self):
        return self.firstName

    def GetMidName(self):
        return self.middleName

    def GetLastName(self):
        return self.lastName

    def SetName(self, firstName, middleName, lastName):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName

        # assume first name is separated by spaces, split into a list
        firstNameList = self.firstName.split()
        # auto-generate an email address based on firstName, middleName, and lastName
        emailConverter = NameToEmail(firstNameList, self.middleName, self.lastName)
        emailConverter.ConvertNameToEmail()
        self.email = emailConverter.GetEmail()

    def GetEmail(self):
        return self.email

    def SetPassword(self, password):
        self.password = password

    def GetPassword(self):
        return self.password

    def isAdmin(self):
        return False