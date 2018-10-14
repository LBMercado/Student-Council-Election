#!/usr/bin/env python

#import modules
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Position import Position

class Party:
    def __init__(self, partyName):
        self.partyName = partyName
        self.candidateDict = {}

        #   initialize all position
        for pos in list(Position):
            strPos = str(pos).split('.')[1]
            self.candidateDict[strPos] = None

    def SetPartyName(self, partyName):
        self.partyName = partyName

    def GetPartyName(self):
        return self.partyName

    def GetCandidateList(self):
        return self.candidateDict.values()

    #   add candidate only if it is not a duplicate or conflicting position
    def AddCandidate(self, newCandidate: Candidate):
        if not isinstance(newCandidate.GetPosition(), Position):
            raise UndefinedPosition('Passed parameter newCandidate'
                                    ' does not have a well-defined position, or is a nonetype.')
        posInStr = str(newCandidate.GetPosition()).split('.')[1]

        #   check if position is unfilled, if not, set the position with the candidate
        if self.candidateDict[posInStr] is None:
            self.candidateDict[posInStr] = newCandidate

    #   set position with new candidate
    def SetCandidate(self, newCandidate: Candidate):
        if not isinstance(newCandidate.GetPosition(), Position):
            raise UndefinedPosition('Passed parameter newCandidate'
                                    ' does not have a well-defined position, or is a nonetype.')

        posInStr = str(newCandidate.GetPosition()).split('.')[1]

        self.candidateDict[posInStr] = newCandidate

    def GetCandidate(self, position: Position):
        posInStr = str(position).split('.')[1]
        return self.candidateDict[posInStr]

    def RemoveCandidate(self, position: Position):
        #search through candidate list and remove candidate with position, if it exists

        posInStr = str(position).split('.')[1]

        self.candidateDict[posInStr] = None

    #   pass a candidateId, returns true if it exists in the candidateDict
    def CandidateExists(self, candidateId):
        if any(candidate.GetUserId() == candidateId for candidate in self.candidateDict.values()):
            return True
        else:
            return False

#   User defined exceptions for easy debugging
class UndefinedPosition(Exception):
    def __init__(self, message):
        super(UndefinedPosition, self).__init__(message)