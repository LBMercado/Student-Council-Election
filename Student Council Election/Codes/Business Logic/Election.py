#!/usr/bin/env python

#import modules
from Party import Party
from Voter import Voter
from VoteTicket import VoterTicket
from datetime import datetime

#Take note that startDate, endDate are of type datetime, it will raise an error if it is not followed
class Election:
    def __init__(self, startDate, parties):
        #take note that startDate should be an object of type datetime
        if type(startDate) is not type(datetime):
            raise TypeError("@" + self.__str__() + ": Unexpected type of parameter startDate: "+ type(startDate)
                            + "\nType should be datetime.")
        self.startDate = startDate
        self.endDate = None
        self.partyList = []
        self.partyList.extend(parties)
        self.voterList = []
        self.voteTicketList = []

    def GetStartDate(self):
        return self.startDate

    def SetEndDate(self, endDate):
        #endDate cannot be before startDate
        if type(endDate) is not type(datetime):
            raise TypeError("@" + self.__str__() + ": Unexpected type of parameter endDate: "+ type(endDate)
                            + "\nType should be datetime.")
        if endDate < self.startDate:
            raise EndDateIsBeforeStartDate("@" + self.__str__() + ": Parameter endDate cannot be before startDate.")
        else:
            self.endDate = endDate

    def GetEndDate(self):
        return self.endDate

    def AddParty(self, party):
        #Add party only if it is not a duplicate
        if party not in self.partyList:
            self.partyList.append(party)

    def GetPartyList(self):
        return self.partyList

    def AddVoter(self, voter):
        #Add voter only if it is not a duplicate
        if voter not in self.voterList:
            self.voterList.append(voter)

    def GetVoterList(self):
        return self.voterList

    def AddVoteTicket(self, voteTicket):
        #Add voteTicket only if it is not a duplicate
        if voteTicket not in self.voteTicketList:
            self.voteTicketList.append(voteTicket)

    def GetVotesFor(self, candidateId):
        #count votes from voteTicket list with condition that candidateId in voteTicket is a match
        voteCount = 0
        candidateIsInList = False

        #candidateId must be in list otherwise, raise an error
        for partyInList in self.partyList:
            for candidateInParty in partyInList:
                if candidateInParty.userId is candidateId:
                    candidateIsInList = True
                    break

        if not candidateIsInList:
            raise ValueError("No candidate match found in " + self.__str__() + " with given id " +
                             "<" + candidateId + ">")

        #Count votes by comparing voteTicket candidateId in voteTicket list and candidateId,
        for voteTicketInList in self.voteTicketList:
            if voteTicketInList.GetCandidateId() is candidateId:
                voteCount += 1
        else:
            return voteCount

#User defined exceptions for easy debugging
class EndDateIsBeforeStartDate(Exception):
    def __init__(self, message):
        super(EndDateIsBeforeStartDate, self).__init__(message)