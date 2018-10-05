#   !/usr/bin/env python

#   import modules
from datetime import datetime
from BusinessLogic.Election import Election
from BusinessLogic.Party import Party
from DataAccess.DataAccess import DataAccess

class ElectionInterface:
    def __init__(self):
        self.data = DataAccess()
        self.election = Election.init_with_null()

    def SetNewElection(self, startDate):
        self.election = Election(startDate)

    def GetElection(self):
        return self.election

    def CheckElection(self):
        startDate = self.data.ReadElectionStartDate()
        if startDate is None:
            return False
        else:
            return True

    def AddParty(self, party):
        self.election.AddParty(party)