#!/usr/bin/env python

#import modules
import Party, Voter, VoteTicket

class Election:
    def __init__(self, startDate, parties):
        self.startDate = startDate
        self.endDate = ""
        self.party = []
        self.party.extend(parties)
        self.voter = []
        self.voteTicket = []

    def GetStartDate(self):
        return self.startDate

    def SetEndDate(self, endDate):
        self.endDate = endDate

    def GetEndDate(self):
        return self.endDate

    def AddParty(self, party):
        self.party.append(party)

    def GetPartyList(self):
        return self.party

    def AddVoter(self, voter):
        self.voter.append(voter)

    def GetVoterList(self):
        return self.voter

    def AddVoteTicket(self, voteTicket):
        self.voteTicket.append(voteTicket)

    def GetVotesFor(self, candidateId):
        #count votes from voteTicket list with condition that candidateId in voteTicket is a match
        pass