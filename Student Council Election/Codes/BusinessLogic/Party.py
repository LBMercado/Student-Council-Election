#!/usr/bin/env python

#import modules
from BusinessLogic.Candidate import Candidate

class Party:
    def __init__(self, partyName):
        self.partyName = partyName
        self.candidateList = []

    def SetPartyName(self, partyName):
        self.partyName = partyName

    def GetPartyName(self):
        return self.partyName

    def GetCandidateList(self):
        return self.candidateList

    def AddCandidate(self, candidate: Candidate):
        #   Add candidate only if it is not a duplicate or conflicting position
        if (candidate not in self.candidateList or
                not any(candidateInList.position == candidate.position for candidateInList in self.candidateList)):
            self.candidateList.append(candidate)

    def GetCandidate(self, position):
        #search through candidate list and return candidate given a position

        for candidateInList in self.candidateList:
            if candidateInList.position == position:
                return candidateInList
        else:
            raise ValueError("No candidate match found in party" + "<" + self.partyName +">" + " with given position "+
                             "<" + position.__str__() + ">")

    def RemoveCandidate(self, position):
        #search through candidate list and remove candidate with position

        for candidateInList in self.candidateList:
            if candidateInList.position == position:
                self.candidateList.remove(candidateInList)
                return
        else:
            raise ValueError("No candidate match found in party " + "<" + self.partyName +">" + " with given position "+
                             "<" + position.__str__() + ">")

    def CandidateExists(self, candidate: Candidate):
        if (candidate in self.candidateList or
                any(candidateInList.position == candidate.position for candidateInList in self.candidateList)):
            return True
        else:
            return False