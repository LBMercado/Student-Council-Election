#!/usr/bin/env python

#import modules
from BusinessLogic.User import User
from BusinessLogic.VoteTicket import VoterTicket

class Voter(User):
    def __init__(self, userId, program, firstName, middleName, lastName, password):
        User.__init__(self, userId, program, firstName, middleName, lastName, password)
        self.voteTicket = []

    def VoteFor(self, candidate):
        #initialize a voter ticket
        newVoteTicket = VoterTicket(self, candidate)

        #keep voteTicket
        self.voteTicket.append(newVoteTicket)

    def GetVoteTickets(self):
        return self.voteTicket