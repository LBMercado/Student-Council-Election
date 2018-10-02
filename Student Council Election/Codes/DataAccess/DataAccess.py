#   !/usr/bin/env python

#   import modules
import sqlite3
from BusinessLogic.User import User
from BusinessLogic.Admin import Admin
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Voter import Voter
from BusinessLogic.Party import Party
from BusinessLogic.Position import Position
from BusinessLogic.Election import Election
from BusinessLogic.VoteTicket import VoterTicket

class DataAccess():
    #   Use :memory: for argument if you want to test database, this stores it in the memory fresh as new
    def __init__(self, dbPath = 'Database\MainDB.db'):
        self.dbPath = dbPath
        self.dbConnection = sqlite3.connect(dbPath)
        self.dbServer = self.dbConnection.cursor()

        #   Initialize new tables if database does not exist yet
        with self.dbConnection:
            #   user table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS user_info(
                                    user_id INTEGER PRIMARY KEY, 
                                    user_program TEXT,
                                    user_firstName TEXT,
                                    user_midName TEXT,
                                    user_lastName TEXT,
                                    user_email TEXT,
                                    user_password TEXT
                                    )
            """)
            #   candidate table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS candidate_info(
                                    user_id INTEGER PRIMARY KEY,
                                    candidate_party TEXT,
                                    candidate_position TEXT,
                                    candidate_platform TEXT
                                    )
            """)
            #   voteTicket table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS vote_ticket(
                                                user_id INTEGER PRIMARY KEY,
                                                candidate_id INTEGER
                                                )
                        """)
            #   election table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS election_info(
                                                            start_date TEXT,
                                                            end_date TEXT
                                                            )
                                    """)

    def __del__(self):
        self.dbConnection.close()

    #   write general class user: voter, candidate, admin
    def WriteUser(self, newUser):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO user_info VALUES(?,?,?,?,?,?,?)", (newUser.GetUserId(), newUser.GetProgram(), newUser.GetFirstName(),
                                                            newUser.GetMidName(), newUser.GetLastName(), newUser.GetEmail(),
                                                            newUser.GetPassword())
                            )

    #   write a new candidate, use this upon registration of user as candidate, promote user to candidate
    def WriteCandidate(self, newCandidate):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO candidate_info VALUES(?,?,?,?)", (newCandidate.GetUserId(), newCandidate.GetParty().GetPartyName(),
                                                                 newCandidate.GetPosition().__str__(), newCandidate.GetPlatform())
                                )

    #   write a new vote ticket into database
    def WriteVoteTicket(self, newVoteTicket):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO vote_ticket VALUES(?,?)",
                (newVoteTicket.GetVoterId(), newVoteTicket.GetCandidateId())
                                )

    #   write new party into database
    def WriteParty(self, newParty):
        with self.dbConnection:
            #   Add a new table representing the party
            self.dbServer.execute(
                "CREATE TABLE IF NOT EXISTS ? (candidate_id INTEGER)", (newParty.GetPartyName(),)
                                )
            #   Add all candidates of the party to the new table
            for candidate in newParty:
                self.dbServer.execute("INSERT OR IGNORE INTO :partyName VALUES(:candidateId)",
                                      {'partyName':newParty.GetPartyName(), 'candidateId': candidate.GetUserId()})

    #   write new election instance into database
    def WriteElection(self, newElection):
        with self.dbConnection:
            #   Insert new instance of election to database
            self.dbServer.execute("INSERT INTO election_info VALUES(:startDate,:endDate)",
                                  {'startDate':newElection.GetStartDate().date(), 'endDate':newElection.GetEndDate().date()})

    #   return user if userId exists in database
    def ReadUser(self, userId):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_id = :idToFind", {'idToFind':userId})
        return self.dbServer.fetchone()

    #   return candidate if userId exists in database
    def ReadCandidate(self, userId):
        self.dbServer.execute("SELECT * FROM candidate_info WHERE user_id = :idToFind", {'idToFind': userId})
        return self.dbServer.fetchone()

    #   return a list of voteTickets corresponding to the candidateId
    def ReadVoteTickets(self, candidateId):
        self.dbServer.execute("SELECT * FROM vote_ticket WHERE user_id = :idToFind", {'idToFind': candidateId})
        return self.dbServer.fetchall()

    #   return a list of candidateIds pertaining to a given party name
    def ReadParty(self, partyName):
        self.dbServer.execute("SELECT * FROM :partyNameToFind", {'partyNameToFind': partyName})
        return self.dbServer.fetchall()

    #   returns a list of all election instances startDate and endDate from database
    def ReadElection(self):
        self.dbServer.execute("SELECT * FROM election_info")
        return self.dbServer.fetchall()

    #   returns true if details exist in database, otherwise false
    def VerifyUser(self, email, password):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_email = :emailToFind AND user_password = :passwordToFind",
                              {'emailToFind': email, 'passwordToFind':password})
        if (self.dbServer.fetchone() is not None):
            return True
        else:
            return False

    #   returns true if user is found, otherwise returns false
    def read_username(self, _user_email):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_email = ? ", (_user_email,))
        if self.dbServer.fetchone() is not None:
            print("Userfound 1")
            return True
        else:
            print("not found 1")
            return False

    #   returns true if userid is found, otherwise returns false
    def read_userId(self, _user_email, _user_password):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_email = ? AND user_password = ?", (_user_email, _user_password))
        if self.dbServer.fetchone() is not None:
            print("YES NAKA LOGIN KA NA!!!!")
            return True
        else:
            print("sad")
            return False

    #   pag palit ng password
    def update_user(self, _user_id, _user_password):
        with self.dbConnection:
            self.dbServer.execute("UPDATE user_info SET user_password = ? WHERE user_id = ? ", (_user_password, _user_id,))