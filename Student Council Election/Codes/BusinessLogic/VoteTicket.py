#!/usr/bin/env python

from BusinessLogic.Position import Position

class VoteTicket:
    def __init__(self, voterId):
        self.voterId = voterId
        self.voteDict = {}

        for pos in list(Position):
            strPos = str(pos).split('.')[1]
            self.voteDict[strPos] = None

    def GetVoterId(self):
        return self.voterId

    def SetVote(self, position: Position, candidateId):
        self.voteDict[str(position).split('.')[1]] = candidateId

    def ClearVote(self, position: Position):
        self.voteDict[str(position).split('.')[1]] = None

    def GetVoteFromPosition(self, position: Position):
        return self.voteDict[str(position).split('.')[1]]

    def GetVoteTicket(self):
        return self.voteDict