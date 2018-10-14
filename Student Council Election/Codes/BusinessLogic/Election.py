#!/usr/bin/env python

#import modules
from datetime import datetime
from BusinessLogic.Party import Party
from BusinessLogic.VoteTicket import VoteTicket
from BusinessLogic.Voter import Voter
from BusinessLogic.Position import Position, Enum
from BusinessLogic.User import User
from DataAccess.DataAccess import DataAccess

#Take note that startDate, endDate are of type datetime, it will raise an error if it is not followed
class Election:
    def __init__(self, startDate, parties = None, dbName = 'MainDB.db'):
        #   take note that startDate should be an object of type datetime
        if startDate is not None and not isinstance(startDate, (datetime)):
            raise TypeError("@" + self.__str__() + ": Unexpected type of parameter startDate."
                            + "\nType should be datetime.")
        self.data = DataAccess(dbName)
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
            readVoterId = str(voter.GetUserId())

            self.voterDict[readVoterId] = voter
            #   init:   get voter ticket
            ticket = self.data.ReadVoteTicketWithUserId(int(readVoterId))

            if ticket is not None:
                self.voterDict[readVoterId].SetVoteTicket(ticket)
                self.voterTicketDict[readVoterId] = ticket
            #   set a new vote ticket if it does not exist in the database
            else:
                newVoteTicket = VoteTicket(int(readVoterId))
                self.voterTicketDict[readVoterId] = newVoteTicket
                self.voterDict[readVoterId].SetVoteTicket(newVoteTicket)

    @classmethod
    def init_with_null(cls):
        return cls(None, None)

    @classmethod
    def init_with_null_and_dbName(cls, dbName):
        return cls(None, None, dbName)

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
        #   add party only if it is not a duplicate
        if party not in self.partyList and not any(partyInList.GetPartyName().lower() == party.GetPartyName().lower() for
                                                   partyInList in self.partyList):
            self.partyList.append(party)

    def GetPartyList(self):
        return self.partyList

    def AddVoter(self, voter: Voter):
        #   voteTicket vote values must contain valid candidateIds
        if not self.VerifyVoteTicket(voter.GetVoteTicket()):
            raise InvalidVote('Some VoteTicket vote candidateIds do not point to a legitimate candidate.')

        #   add voter only if it is not a duplicate
        if str(voter.GetUserId()) not in self.voterDict:
            self.voterDict[str(voter.GetUserId())] = voter
            #   check if user has a vote ticket, otherwise initialize it
            if str(voter.GetUserId()) not in self.voterTicketDict:
                self.voterTicketDict[str(voter.GetUserId())] = VoteTicket(voter.GetUserId())
            else:
                self.voterTicketDict[str(voter.GetUserId())] = voter.GetVoteTicket()

    def AddVoteTicket(self, voteTicket: VoteTicket):
        #   voteTicket vote values must contain valid candidateIds
        if not self.VerifyVoteTicket(voteTicket):
            raise InvalidVote('Some VoteTicket vote candidateIds do not point to a legitimate candidate.')

        #   add voteTicket only if it is not a duplicate, and user exists in voterDict
        if str(voteTicket.GetVoterId()) not in self.voterTicketDict and \
                str(voteTicket.GetVoterId()) in self.voterDict:
            self.voterTicketDict[str(voteTicket.GetVoterId())] = voteTicket.GetVoterId()
            self.voterDict[str(voteTicket.GetVoterId())].SetVoteTicket(voteTicket)

    #   gets corresponding Voter object based on the given voterId, or return None if it does not exist
    def GetVoter(self, voterId):
        if str(voterId) in self.voterDict:
            return self.voterDict[str(voterId)]
        else:
            return None

    #   gets corresponding VoteTicket object based on the given voterId, or return None if it does not exist
    def GetVoterTicket(self, voterId):
        if str(voterId) in self.voterTicketDict:
            return self.voterTicketDict[str(voterId)]
        else:
            return None
    def GetVoterList(self):
        return self.voterDict.values()

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

    #   update Voters and their voteTickets in database
    def UpdateVoters(self):
        #   don't update if there is nothing to update
        #   don't update if there are no voters
        #   dictionaries evaluate to false when empty, true otherwise
        if not self.voterTicketDict or not self.voterDict:
            #   update all voteTicket objects in database
            for voter in self.voterDict.values():
                voterUser = User(voter.GetUserId(), voter.GetProgram(), voter.GetFirstName(),
                                 voter.GetMidName(), voter.GetLastName(), voter.GetPassword())
                self.data.WriteOrUpdateUser(voterUser)
                #   update all voterDicts in Database
                #   voteTicket contains a dictionary, that's what's needed
                self.data.WriteVoteTicket(voter.GetUserId(), voter.GetVoteTicket().GetVoteTicket())

    #   update vote tickets in database
    def UpdateVoteTickets(self):
        #   don't update if there is nothing to update
        #   don't update if there are no voters
        #   dictionaries evaluate to false when empty, true otherwise
        if not self.voterTicketDict or not self.voterDict:
            for vt in self.voterTicketDict.values():
                self.data.WriteVoteTicket(vt.GetVoterId(), vt.GetVoteTicket())

    #   syncs the voter with the voterDict and voterTicketDict, otherwise, it does nothing
    def UpdateVoter(self, updatedVoter: Voter):
        #   voteTicket vote values must contain valid candidateIds
        if not self.VerifyVoteTicket(updatedVoter.GetVoteTicket()):
            raise InvalidVote('Some VoteTicket vote candidateIds do not point to a legitimate candidate.')

        #   update the voter in voterDict if it exists
        if str(updatedVoter.GetUserId()) in self.voterDict and str(updatedVoter.GetUserId()) in self.voterTicketDict:
            self.voterDict[str(updatedVoter.GetUserId())] = updatedVoter
            self.voterTicketDict[str(updatedVoter.GetUserId())] = updatedVoter.GetVoteTicket()
            #   reflect changes in database
            self.data.UpdateUser(updatedVoter.get_user_equivalent())
            #   voteTicket contains a dictionary, that's what's needed
            self.data.WriteVoteTicket(updatedVoter.GetUserId(), updatedVoter.GetVoteTicket().GetVoteTicket())

    #   syncs the voterTicket with the voterDict and voterTicketDict, otherwise, it does nothing
    def UpdateVoteTicket(self, updatedVoteTicket: VoteTicket):
        #   voteTicket vote values must contain valid candidateIds
        if not self.VerifyVoteTicket(updatedVoteTicket):
            raise InvalidVote('Some VoteTicket vote candidateIds do not point to a legitimate candidate.')

        if str(updatedVoteTicket.GetVoterId()) in self.voterDict\
                and str(updatedVoteTicket.GetVoterId()) in self.voterTicketDict:
            self.voterTicketDict[str(updatedVoteTicket.GetVoterId())] = updatedVoteTicket
            self.voterDict[str(updatedVoteTicket.GetVoterId())].SetVoteTicket(updatedVoteTicket)

            #   reflect changes in database
            #   voteTicket contains a dictionary, that's what's needed
            self.data.WriteVoteTicket(updatedVoteTicket.GetVoterId(), updatedVoteTicket.GetVoteTicket())

    #   return true if ticket is valid, otherwise it returns false
    #   condition for valid ticket:
    #   every vote must point to None or a valid candidateId
    #   every position and its candidate id must match the position that the candidate is pursuing for
    def VerifyVoteTicket(self, voteTicket: VoteTicket):
        voteDict = voteTicket.GetVoteTicket()

        #   the candidateId must exist in one of the parties
        candidateList = []
        for party in self.partyList:
            filteredCandidateList = filter(lambda cand:cand is not None, party.GetCandidateList())
            candidateList.extend(filteredCandidateList)

        #   go through all the all possible vote entries in the ticket
        for candidatePosition in voteDict.keys():
            #   go to next in sequence if it is set as none (abstain vote)
            if voteDict[candidatePosition] is None or voteDict[candidatePosition] == '':
                continue

            #   the candidateId must exist in one of the parties
            if not any(candidate.GetUserId() == voteDict[candidatePosition] for candidate in candidateList):
                return False

            #   iterate through each candidate list in each party,
            #   there MUST BE a matching candidate, otherwise return false
            candidateFound = False

            for party in self.partyList:
                pos = Position[candidatePosition]
                #   check if voting for a ghost candidate, or a mismatched position, or a candidateId that does not
                #   match the id of the candidate
                candidateInParty = party.GetCandidate(pos)
                if candidateInParty is not None and \
                        candidateInParty.GetPosition() == pos and \
                        candidateInParty.GetUserId() == voteDict[candidatePosition]:
                    candidateFound = True

            return candidateFound
        #   hmmmm, candidate has no votes... this is till valid though
        else:
            return True

#   User defined exceptions for easy debugging
class EndDateIsBeforeStartDate(Exception):
    def __init__(self, message):
        super(EndDateIsBeforeStartDate, self).__init__(message)

class UndefinedStartDate(Exception):
    def __init__(self, message):
        super(UndefinedStartDate, self).__init__(message)

class InvalidVote(Exception):
    def __init__(self, message):
        super(InvalidVote, self).__init__(message)