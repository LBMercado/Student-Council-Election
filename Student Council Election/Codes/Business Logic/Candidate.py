#!/usr/bin/env python

#import modules
import User.py

class Candidate(User):
    def __init__(self, id, firstName, middleName, lastName, email, position, party):
        User.__init__(self, id, firstName, middleName, lastName, email)
        self.position = position
        self.party = party
        self.platform = ""

    def SetPosition(self, position):
        self.position = position

    def GetPosition(self):
        return self.position

    def SetParty(self, party):
        self.party = party

    def GetParty(self):
        return self.party

    def SetPlatform(self, platform):
        self.platform = platform

    def GetPlatform(self):
        return self.platform