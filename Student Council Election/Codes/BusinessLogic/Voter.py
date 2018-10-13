#!/usr/bin/env python

#import modules
from BusinessLogic.User import User
from BusinessLogic.VoteTicket import VoteTicket
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Position import Position

class Voter(User):
    def __init__(self, userId, program, firstName, middleName, lastName, password):
        User.__init__(self, userId, program, firstName, middleName, lastName, password)
        self.voteTicket = VoteTicket(self.userId)

    @classmethod
    def morph_user_to_voter(cls, user: User):
        return cls(user.GetUserId(), user.GetProgram(), user.GetFirstName(), user.GetMidName(),
                   user.GetLastName(), user.GetPassword())

    def SetVoteTicket(self, voteTicket):
        self.voteTicket = voteTicket

    def VoteFor(self, candidateId, position: Position):
        #   set candidate to appropriate position in voteTicket
        self.voteTicket.SetPositionWithCandidateId(position, candidateId)

    def GetVoteTicket(self):
        return self.voteTicket