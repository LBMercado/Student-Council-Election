#!/usr/bin/env python

#import modules
from DataLogic import read_username
from DataLogic import write_user
from DataLogic import read_userid

class User:
    def __init__(self, id = "19991234567", program = "CPE", firstName = "John", middleName = "Parker", lastName = "Doe",
                 email = "jpdoe@mymail.mapua.edu.ph", password = "19991234567"):
        self.id = id
        self.program = program
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.email = email
        self.password = password

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetProgram(self, program):
        self.program = program

    def GetProgram(self):
        return self.program

    def SetFirstName(self, firstName):
        self.firstName = firstName

    def GetFirstName(self):
        return self.firstName

    def SetMidName(self, middleName):
        self.middleName = middleName

    def GetMidName(self):
        return self.middleName

    def SetLastName(self, LastName):
        self.lastName = LastName

    def GetLastName(self):
        return self.lastName

    def SetEmail(self, email):
        self.email = email

    def GetEmail(self):
        return self.email

    def SetPassword(self, password):
        self.password = password

    def GetPassword(self):
        return self.password
    
    def userExists(self):
        #fullName = self.lastName + ", " + self.firstName + "(" + self.middleName + ")"
        #fullName = fullName.upper()
        #return read_user(fullName, self.id)
        return read_username(self.lastName)
    
    def userIDExists(self):
        return read_userid(self.lastName, self.password)