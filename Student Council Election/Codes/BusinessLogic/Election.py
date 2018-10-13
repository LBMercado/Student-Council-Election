#!/usr/bin/env python

#import modules
from datetime import datetime
from BusinessLogic.Party import Party
from BusinessLogic.VoteTicket import VoteTicket
from BusinessLogic.Voter import Voter
from BusinessLogic.Position import Position
from DataAccess.DataAccess import DataAccess

#Take note that startDate, endDate are of type datetime, it will raise an error if it is not followed
class Election:
    def __init__(self, startDate, parties = None):
        #   take note that startDate should be an object of type datetime
        if startDate is not None and not isinstance(startDate, (datetime)):
            raise TypeError("@" + self.__str__() + ": Unexpected type of parameter startDate."
                            + "\nType should be datetime.")
        self.data = DataAccess()
        self.startDate = startDate
        self.endDate = None
        self.partyList = []
        if parties is not None:
            self.partyList.extend(parties)
        self.voterDict = {}
        self.voterTicketDict = {}

        #   initialize values for each in database

        #   init: get party members for each and initialize Party objects
        for partyName in self.data.ReadAllPartyNames():
            party = Party(partyName)
            for cand in self.data.ReadAllPartyCandidates(partyName):
                party.AddCandidate(cand)
            self.partyList.append(party)

        #   init: get all voters
        for voter in self.data.ReadAllVoters():
            self.voterDict[str(voter.GetUserId())] = voter

        #   init: get all voter tickets
        for ticket in self.data.ReadAllVoteTickets():
            self.voterTicketDict[str(ticket.GetVoterId())] = ticket

    @classmethod
    def init_with_null(cls):
        return cls(None, None)

    @classmethod
    def init_with_startAndEndDate(cls, startDate, endDate):
        cls(startDate, None)
        cls.endDate = endDate
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

    def AddVoter(self, voter: Voter):
        #Add voter only if it is not a duplicate
        if voter.GetUserId() not in self.voterDict:
            self.voterDict[str(voter.GetUserId())] = voter

    def GetVoterList(self):
        return self.voterDict

    def AddVoteTicket(self, voteTicket: VoteTicket):
        #Add voteTicket only if it is not a duplicate
        if voteTicket.GetVoterId() not in self.voterTicketDict:
            self.voterTicketDict[str(voteTicket.GetVoterId())] = voteTicket

    #   count votes from voteTicket list with condition that candidateId in voteTicket is a match
    def GetVotesFor(self, candidateId):
        voteCount = 0
        candidateIsInList = False
        candPosition = None

        #   candidateId must be in list otherwise, raise an error
        for partyInList in self.partyList:
            for candidateInParty in partyInList.GetCandidateList():
                if candidateInParty.userId is candidateId:
                    candPosition = candidateInParty.GetPosition()
                    candidateIsInList = True
                    break
            if candidateIsInList:
                break

        if not candidateIsInList:
            raise ValueError("No candidate match found in " + self.__str__() + " with given id " +
                             "<" + (str)(candidateId) + ">")

        #   count votes by comparing voteTicket candidateId in voteTicket list and candidateId
        for voteTicket in self.voterTicketDict.values():
            if voteTicket.GetVoteFromPosition(candPosition) == candidateId:
                voteCount += 1
        else:
            return voteCount

    #   update vote tickets in database
    def UpdateVoteTickets(self):

        #   don't update if there is nothing to update
        #   don't update if there are no voters
        if len(self.voterTicketDict) is 0 or len(self.voterDict) is 0:
            for vt in self.voterTicketDict.values():
                self.data.WriteVoteTicket(vt.GetVoterId(), vt.GetVoteTicket())

    #   syncs the voter with the voterDict and voterTicketDict, otherwise, it does nothing
    def UpdateVoter(self, updatedVoter: Voter):
        #   update the voter in voterDict
        if str(updatedVoter.GetUserId()) in self.voterDict and str(updatedVoter.GetUserId()) in self.voterTicketDict:
            self.voterDict[str(updatedVoter.GetUserId())] = Voter
            self.voterTicketDict[str(updatedVoter.GetUserId())] = Voter.GetVoteTicket()
            #   reflect changes in database
            self.data.UpdateUser(updatedVoter)
            self.UpdateVoteTickets()

#   User defined exceptions for easy debugging
class EndDateIsBeforeStartDate(Exception):
    def __init__(self, message):
        super(EndDateIsBeforeStartDate, self).__init__(message)

class UndefinedStartDate(Exception):
    def __init__(self, message):
        super(UndefinedStartDate, self).__init__(message)