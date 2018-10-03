#!/usr/bin/env python

#import modules
from BusinessLogic.User import User
from BusinessLogic.VoteTicket import VoterTicket
from BusinessLogic.Candidate import Candidate

class Voter(User):
    def __init__(self, userId, program, firstName, middleName, lastName, password):
        User.__init__(self, userId, program, firstName, middleName, lastName, password)
        self.voteTicket = []

    def VoteFor(self, candidate: Candidate):
        #   initialize a voter ticket
        newVoteTicket = VoterTicket(self.userId, candidate.GetUserId())

        #   keep vote ticket, but make sure it is not a duplicate
        if not any(ticketInList.GetCandidateId() == candidate.GetUserId() for ticketInList in self.voteTicket):
            self.voteTicket.append(newVoteTicket)

    def GetVoteTickets(self):
        return self.voteTicket