#!/usr/bin/env python

class VoterTicket:
    def __init__(self, voterId, candidateId):
        self.voterId = voterId
        self.candidateId = candidateId

    def GetVoterId(self):
        return self.voterId

    def GetCandidateId(self):
        return self.candidateId