#!/usr/bin/env python

#import modules
import User, Candidate

class VoterTicket:
    def __init__(self, voter, candidate):
        self.voterId = voter.id
        self.candidateId = candidate.id

    def GetVoterId(self):
        return self.voterId

    def GetCandidateId(self):
        return self.candidateId