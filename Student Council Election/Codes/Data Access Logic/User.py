#!/usr/bin/env python

#import modules

class User:
    def __init__(self):
        self.id = 0
        self.firstName = "John"
        self.middleName = "P"
        self.lastName = "Doe"
        self.email = "jpdoe@mymail.mapua.edu.ph"

    def __init__(self, id,firstName, middleName, lastName, email):
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.email = email

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

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