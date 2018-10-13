#!/usr/bin/env python

#import modules
from BusinessLogic.NameToEmail import NameToEmail

class User:
    def __init__(self, userId, program, firstName, middleName, lastName, password = None):
        self.userId = userId
        self.program = program

        if firstName is not None and middleName is not None and lastName is not None:
            self.firstName = firstName.upper()
            self.middleName = middleName.upper()
            self.lastName = lastName.upper()

            # assume first name is separated by spaces, split into a list
            firstNameList = self.firstName.split()
            # auto-generate an email address based on firstName, middleName, and lastName
            emailConverter = NameToEmail(firstNameList, self.middleName, self.lastName)
            emailConverter.ConvertNameToEmail()
            self.email = emailConverter.GetEmail()
        else:
            self.firstName = firstName
            self.middleName = middleName
            self.lastName = lastName

        #If no supplied password, default password is userId
        if password is None:
            self.password = userId
        else:
            self.password = password

    @classmethod
    def init_with_email_and_password(cls, email, password):
        userId = None
        program = None
        firstName = None
        middleName = None
        lastName = None
        cls.email = email
        return cls(userId, program, firstName, middleName, lastName, password)

    @classmethod
    def init_with_userId(cls, userId):
        userId = userId
        program = None
        firstName = None
        middleName = None
        lastName = None
        password = None
        return cls(userId, program, firstName, middleName, lastName, password)

    @classmethod
    def init_with_null(cls):
        userId = None
        program = None
        firstName = None
        middleName = None
        lastName = None
        password = None
        return cls(userId, program, firstName, middleName, lastName, password)

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