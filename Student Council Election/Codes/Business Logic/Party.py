#!/usr/bin/env python

#import modules
from Candidate import Candidate

class Party:
    def __init__(self, partyName):
        self.partyName = partyName
        self.candidateList = []

    def SetPartyName(self, partyName):
        self.partyName = partyName

    def GetPartyName(self):
        return self.partyName

    def AddCandidate(self, candidate):
        #Add candidate only if it is not a duplicate or conflicting position
        if (candidate not in self.candidateList or
                not any(candidateInList.position == candidate.position for candidateInList in self.candidateList)):
            self.candidateList.append(candidate)
        else:
            pass

    def GetCandidate(self, position):
        #search through candidate list and return candidate given a position
        for candidateInList in self.candidateList:
            if candidateInList.position == position:
                return candidateInList
        else:
            raise ValueError("No candidate match found in " + "<" + self.partyName +">" + " with given position "+
                             "<" + position + ">")

    def RemoveCandidate(self, position):
        #search through candidate list and remove candidate with position
        for candidateInList in self.candidateList:
            if candidateInList.position == position:
                self.candidateList.remove(candidateInList)
        else:
            raise ValueError("No candidate match found in " + "<" + self.partyName +">" + " with given position "+
                             "<" + position + ">")