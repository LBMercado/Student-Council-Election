#!/usr/bin/env python

#import modules
from BusinessLogic.User import User
from BusinessLogic.Position import Position

class Candidate(User):
    def __init__(self, userId, program, firstName, middleName, lastName, password, position, partyName):
        User.__init__(self, userId, program, firstName, middleName, lastName, password)

        if not isinstance(position, Position):
            raise TypeError("@" + self.__str__() + ": Unexpected type of parameter position." +
                            + "\nType should be Position.")

        #position is an Enum, look at Position class for possible values
        self.position = position

        #this is the name of the party of the candidate
        self.partyName = partyName

        self.platform = "This candidate has no platform at this time."

        self.picturePath = ''

    def SetPosition(self, position):
        self.position = position

    def GetPosition(self):
        return self.position

    def SetPartyName(self, party):
        self.partyName = party

    def GetPartyName(self):
        return self.partyName

    def SetPlatform(self, platform):
        self.platform = platform

    def GetPlatform(self):
        return self.platform

    def SetPicturePath(self, picturePath):
        self.picturePath = picturePath

    def GetPicturePath(self):
        return self.picturePath