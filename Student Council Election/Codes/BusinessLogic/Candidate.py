#!/usr/bin/env python

#import modules
from BusinessLogic.User import User
from BusinessLogic.Position import Position

class Candidate(User):
    def __init__(self, userId, program, firstName, middleName, lastName, password, position, party):
        User.__init__(self, userId, program, firstName, middleName, lastName, password)

        if not isinstance(position, Position):
            raise TypeError("@" + self.__str__() + ": Unexpected type of parameter position." +
                            + "\nType should be Position.")

        #position is an Enum, look at Position class for possible values
        self.position = position

        #this is the name of the party of the candidate
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