#!/usr/bin/env python

#import modules
from User import User

class Candidate(User):
    def __init__(self, userId, program, firstName, middleName, lastName, password, position, party):
        User.__init__(self, userId, program, firstName, middleName, lastName, password)
        self.position = position
        self.party = party
        self.platform = "This candidate has no platform at this time."

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