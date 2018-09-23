#!/usr/bin/env python

#import modules
import Candidate

class Party:
    def __init__(self, partyName):
        self.partyName = partyName
        self.candidate = []

    def SetPartyName(self, partyName):
        self.partyName = partyName

    def GetPartyName(self):
        return self.partyName

    def AddCandidate(self, candidate):
        #have to make sure it's not a duplicate
        self.candidate.append(candidate)

    def GetCandidate(self, position):
        #search through candidate list and return candidate with position
        #return true if successful, otherwise false
        pass

    def RemoveCandidate(self, position):
        #search through candidate list and remove candidate with position
        #return true if successful, otherwise false
        pass