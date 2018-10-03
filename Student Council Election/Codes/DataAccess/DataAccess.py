#   !/usr/bin/env python

#   import modules
import sqlite3
from BusinessLogic.User import User
from BusinessLogic.NameToEmail import NameToEmail
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Party import Party
from BusinessLogic.Position import Position
from BusinessLogic.Election import Election
from BusinessLogic.VoteTicket import VoterTicket
from datetime import datetime
import csv

class DataAccess():
    #   Use :memory: for argument if you want to test database, this stores it in the memory fresh as new
    def __init__(self, dbName = 'MainDB.db'):
        if dbName == ':memory:':
            self.dbPath = dbName
        else:
            self.dbPath = 'Database/' + dbName
        self.dbConnection = sqlite3.connect(self.dbPath)
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

            self.dbServer.execute("SELECT COUNT(*) FROM user_info LIMIT 1")
            returnedRow = self.dbServer.fetchone()
            #   don't reinitialize user_info if it is already initialized
            if returnedRow is None:
                with open('Resources/user_info_complete_with_pass.csv', 'r') as openFile:
                    dataRead = csv.DictReader(openFile)
                    to_db = [(i['user_id'].replace(' ', ''), i['user_program'], i['user_firstName'], i['user_midName'],
                              i['user_lastName'], i['user_email'], i['user_password']) for i in dataRead]
                to_db.pop()  # get that weird last entry off the list
                self.dbServer.executemany('INSERT OR IGNORE INTO user_info VALUES(?,?,?,?,?,?,?)', to_db)

                #   form the emails of the users
                userList = self.ReadUsers()
                for user in userList:
                    self.UpdateUser(user)

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

    #   starts a new database connection
    def newConnection(self, dbName):
        #   close existing connection
        self.dbConnection.close()

        if dbName == ':memory:':
            self.dbPath = dbName
        else:
            self.dbPath = 'Database/' + dbName
        self.dbConnection = sqlite3.connect(self.dbPath)
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
            self.dbServer.execute("SELECT COUNT(*) FROM user_info LIMIT 1")
            returnedRow = self.dbServer.fetchone()
            #   don't reinitialize user_info if it is already initialized
            if returnedRow is not None:
                with open('Resources/user_info_complete_with_pass.csv', 'r') as openFile:
                    dataRead = csv.DictReader(openFile)
                    to_db = [(i['user_id'].replace(' ', ''), i['user_program'], i['user_firstName'], i['user_midName'],
                              i['user_lastName'], i['user_email'], i['user_password']) for i in dataRead]
                to_db.pop()  # get that weird last entry off the list
                self.dbServer.executemany('INSERT OR IGNORE INTO user_info VALUES(?,?,?,?,?,?,?)', to_db)

                #   form the emails of the users
                userList = self.ReadUsers()
                for user in userList:
                    self.UpdateUser(user)
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
    def WriteUser(self, newUser: User):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO user_info VALUES(?,?,?,?,?,?,?)", (newUser.GetUserId(), newUser.GetProgram(), newUser.GetFirstName(),
                                                            newUser.GetMidName(), newUser.GetLastName(), newUser.GetEmail(),
                                                            newUser.GetPassword())
                            )

    #   update general class user: voter, candidate, admin
    def UpdateUser(self, existingUser: User):
        with self.dbConnection:
            self.dbServer.execute(
                """UPDATE user_info SET user_program = ?, user_firstName = ?, user_midName = ?, 
                user_lastName = ?, user_email = ?, user_password = ? WHERE user_id = ?""",
                (existingUser.GetProgram(), existingUser.GetFirstName(),
                 existingUser.GetMidName(), existingUser.GetLastName(), existingUser.GetEmail(),
                 existingUser.GetPassword(), existingUser.GetUserId())
                                )

    #   write a new candidate, use this upon registration of user as candidate, promote user to candidate
    def WriteCandidate(self, newCandidate: Candidate):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO candidate_info VALUES(?,?,?,?)", (newCandidate.GetUserId(), newCandidate.GetParty().GetPartyName(),
                                                                 newCandidate.GetPosition().__str__(), newCandidate.GetPlatform())
                                )

    #   write a new vote ticket into database
    def WriteVoteTicket(self, newVoteTicket: VoterTicket):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO vote_ticket VALUES(?,?)",
                (newVoteTicket.GetVoterId(), newVoteTicket.GetCandidateId())
                                )

    #   write party candidates into database
    def WritePartyCandidates(self, newParty: Party):
        with self.dbConnection:
            #   Add all candidates of the party to the new table
            for candidate in newParty.GetCandidateList():
                self.dbServer.execute("INSERT OR IGNORE INTO :partyName VALUES(:candidateId)",
                                      {'partyName':newParty.GetPartyName(), 'candidateId': candidate.GetUserId()})

    #   write new election instance into database
    #   WARNING: THIS WILL CREATE A NEW DATABASE, MAKE SURE TO HANDLE THIS PROPERLY
    def WriteNewElection(self, newElection: Election):
        #   open a new database named election_<startdate>
        self.newConnection('election_' + ''.join(str(newElection.GetStartDate().date()).split('-')) + '.db')

        with self.dbConnection:
            #   insert new instance of election to database
            self.dbServer.execute("INSERT INTO election_info VALUES(:startDate,:endDate)",
                                  {'startDate':newElection.GetStartDate().date(),
                                   'endDate':newElection.GetEndDate().date()})

            #   load into database user_info values

    #   load database corresponding to startDate
    def ReadExistingElection(self, startDate: datetime):
        self.newConnection('election_' + ''.join(str(startDate.date()).split('-')) + '.db')

    #   return user if userId exists in database
    def ReadUser(self, userId):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_id = :idToFind", {'idToFind':userId})
        userDetails = self.dbServer.fetchone()
        if userDetails is not None:
            #   userDetails[5] is email, not needed for defining User
            returnUser = User(int(userDetails[0]), userDetails[1], userDetails[2], userDetails[3], userDetails[4],
                              userDetails[6])
            return returnUser
        else:
            return None

    #   return a list of User instances from database
    def ReadUsers(self):
        self.dbServer.execute("SELECT user_id FROM user_info")
        fetchedIds = self.dbServer.fetchall()
        if fetchedIds is not None:
            #   userDetails[5] is email, not needed for defining User
            returnUserList = []
            for fetchedId in fetchedIds:
                returnUserList.append(self.ReadUser(fetchedId[0]))
            return returnUserList
        else:
            return None

    #   return candidate if userId exists in database
    def ReadCandidate(self, userId):
        returnUser = self.ReadUser(userId)
        if returnUser is not None:
            #   get candidate details
            self.dbServer.execute("SELECT * FROM candidate_info WHERE user_id = :idToFind",
                                                     {'idToFind': userId})
            candidateDetails = self.dbServer.fetchone()
            #   check if user is a candidate
            if candidateDetails is not None:
                candidateParty = Party(candidateDetails[1])
                returnCandidate = Candidate(returnUser.GetUserId(), returnUser.GetProgram(), returnUser.GetFirstName(),
                                            returnUser.GetMidName(),returnUser.GetLastName(),returnUser.GetPassword(),
                                            Position[candidateDetails[2].split('.')[1]], candidateParty)
                returnCandidate.SetPlatform(candidateDetails[3])
                return returnCandidate
            else:
                return None
        else:
            return None

    #   return a list of voteTickets corresponding to the candidateId
    def ReadVoteTickets(self, candidateId):
        self.dbServer.execute("SELECT * FROM vote_ticket WHERE user_id = :idToFind",
                              {'idToFind': candidateId})
        voteTickDetailsList = self.dbServer.fetchall()
        if voteTickDetailsList is not None:
            returnTickets = []
            #   instantiate each ticket as VoteTicket
            for voteTickDetails in voteTickDetailsList:
                voteTicket = VoterTicket(voteTickDetails[0], voteTickDetails[1])
                returnTickets.append(voteTicket)
            return returnTickets
        else:
            return None

    #   return a list of candidateIds pertaining to a given party name
    def ReadPartyCandidates(self, partyName):
        #   partyName is case-sensitive
        self.dbServer.execute("SELECT user_id FROM candidate_info WHERE candidate_party = :partyNameToFind",
                              {'partyNameToFind': partyName})
        returnCandList = []
        candidateIdReadList = self.dbServer.fetchall()
        for candidateIdRead in candidateIdReadList:
            returnCandList.append(self.ReadCandidate(candidateIdRead))

        if len(returnCandList) == 0:
            return None
        else:
            return returnCandList

    #   returns a list containing startDate and endDate
    def ReadElectionDates(self):
        self.dbServer.execute("SELECT * FROM election_info")
        electionDetails = self.dbServer.fetchone()
        startDate = datetime.strptime(electionDetails[0],"%Y-%m-%d")
        if electionDetails[1] == 'NO_END':
            endDate = None
        else:
            endDate = datetime.strptime(electionDetails[1],"%Y-%m-%d")

        return [startDate, endDate]

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
            return True
        else:
            return False

    #   returns true if userid is found, otherwise returns false
    def read_userId(self, _user_email, _user_password):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_email = ? AND user_password = ?", (_user_email, _user_password))
        if self.dbServer.fetchone() is not None:
            return True
        else:
            return False

    #   pag palit ng password
    def update_user(self, _user_id, _user_password):
        with self.dbConnection:
            self.dbServer.execute("UPDATE user_info SET user_password = ? WHERE user_id = ? ", (_user_password, _user_id,))