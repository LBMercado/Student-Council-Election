#!/usr/bin/env python

from NameToEmail import NameToEmail

class User:
    def __init__(self, userId, program, firstName, middleName, lastName):
        self.userId = userId
        self.program = program
        self.firstName = firstName.lower()
        self.middleName = middleName.lower()
        self.lastName = lastName.lower()

        # assume first name is separated by spaces, split into a list
        firstNameList = self.firstName.split()
        # auto-generate an email address based on firstName, middleName, and lastName
        emailConverter = NameToEmail(firstNameList, self.middleName, self.lastName)
        emailConverter.ConvertNameToEmail()
        self.email = emailConverter.GetEmail()

    def SetUserId(self, userId):
        self.userId = userId

    def GetUserId(self):
        return self.userId

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

    def SetEmail(self, email):
        self.email = email

    def GetEmail(self):
        return self.email