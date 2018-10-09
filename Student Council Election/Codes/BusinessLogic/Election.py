#!/usr/bin/env python

#import modules
from datetime import datetime
from BusinessLogic.Party import Party
from DataAccess.DataAccess import DataAccess

#Take note that startDate, endDate are of type datetime, it will raise an error if it is not followed
class Election:
    def __init__(self, startDate, parties = None):
        #   take note that startDate should be an object of type datetime
        if not isinstance(startDate, (datetime)) and startDate is not None :
            raise TypeError("@" + self.__str__() + ": Unexpected type of parameter startDate."
                            + "\nType should be datetime.")
        self.data = DataAccess()
        self.startDate = startDate
        self.endDate = None
        self.partyList = []
        if parties is not None:
            self.partyList.extend(parties)
        self.voterList = []
        self.voteTicketList = []

    @classmethod
    def init_with_null(cls):
        return cls(None, None)

    @classmethod
    def init_with_startAndEndDate(cls, startDate, endDate):
        cls(startDate, None)
        cls.SetEndDate(endDate)
        return cls

    #   return true if election table is filled, otherwise false
    @staticmethod
    def ElectionExists():
        data = DataAccess()
        if data.ReadElectionStartDate() is not None:
            return True
        else:
            return False

    #   return existing election start date, if it exists
    @staticmethod
    def GetExistingElectionStartDate():
        data = DataAccess()
        return data.ReadElectionStartDate()

    @staticmethod
    def GetExistingElectionEndDate():
        data = DataAccess()
        return data.ReadElectionEndDate()

    @staticmethod
    def DropExistingElection():
        data = DataAccess()
        data.EndElection()

    def GetStartDate(self):
        return self.startDate

    def SetEndDate(self, endDate):
        #   check if endDate is not none
        if self.startDate is not None:
            #   endDate cannot be before startDate
            if not isinstance(endDate, (datetime)):
                raise TypeError("@" + self.__str__() + ": Unexpected type of parameter endDate: "
                                + "\nType should be datetime.")
            if endDate < self.startDate:
                raise EndDateIsBeforeStartDate("@" + self.__str__() + ": Parameter endDate cannot be before startDate.")
            else:
                self.endDate = endDate
        else:
            raise UndefinedStartDate('Start Date has not been set.')

    #   write start and end election to database
    def StartElection(self):
        if self.startDate is not None and self.endDate is not None:
            self.data.WriteNewElection(self.startDate, self.endDate)

    def GetEndDate(self):
        return self.endDate

    def AddParty(self, party):
        #Add party only if it is not a duplicate
        if party not in self.partyList and not any(partyInList.GetPartyName().lower() == party.GetPartyName().lower() for
                                                   partyInList in self.partyList):
            self.partyList.append(party)

    def GetPartyList(self):
        return self.partyList

    def AddVoter(self, voter):
        #Add voter only if it is not a duplicate
        if voter not in self.voterList and not \
                any(voterInList.GetUserId() == voter.GetUserId() for voterInList in self.voterList):
            self.voterList.append(voter)

    def GetVoterList(self):
        return self.voterList

    def AddVoteTicket(self, voteTicket):
        #Add voteTicket only if it is not a duplicate
        if not any(voteTicketInList.GetVoterId() == voteTicket.GetVoterId() and voteTicketInList.GetCandidateId() == voteTicket.GetCandidateId()
                   for voteTicketInList in self.voteTicketList):
            self.voteTicketList.append(voteTicket)

    def GetVotesFor(self, candidateId):
        #count votes from voteTicket list with condition that candidateId in voteTicket is a match
        voteCount = 0
        candidateIsInList = False

        #candidateId must be in list otherwise, raise an error
        for partyInList in self.partyList:
            for candidateInParty in partyInList.GetCandidateList():
                if candidateInParty.userId is candidateId:
                    candidateIsInList = True
                    break

        if not candidateIsInList:
            raise ValueError("No candidate match found in " + self.__str__() + " with given id " +
                             "<" + candidateId.__str__() + ">")

        #Count votes by comparing voteTicket candidateId in voteTicket list and candidateId,
        for voteTicketInList in self.voteTicketList:
            if voteTicketInList.GetCandidateId() is candidateId:
                voteCount += 1
        else:
            return voteCount

#   User defined exceptions for easy debugging
class EndDateIsBeforeStartDate(Exception):
    def __init__(self, message):
        super(EndDateIsBeforeStartDate, self).__init__(message)

class UndefinedStartDate(Exception):
    def __init__(self, message):
        super(UndefinedStartDate, self).__init__(message)