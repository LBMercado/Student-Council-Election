#!/usr/bin/env python

#import modules
from NameToEmail import NameToEmail
from DataLogic import read_username
from DataLogic import write_user
from DataLogic import read_userid

class User:
    def __init__(self, userId, program, firstName, middleName, lastName, password):
        self.userId = userId
        self.program = program
        self.firstName = firstName.lower()
        self.middleName = middleName.lower()
        self.lastName = lastName.lower()
		self.password = password

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

    def SetProgram(self, program):
        self.program = program

    def GetProgram(self):
        return self.program

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

    def SetPassword(self, password):
        self.password = password

    def GetPassword(self):
        return self.password
    
    def userExists(self):
        return read_username(self.lastName)
    
    def userIDExists(self):
        return read_userid(self.lastName, self.password)