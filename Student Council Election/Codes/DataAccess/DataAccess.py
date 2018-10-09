#   !/usr/bin/env python

#   import modules
import sqlite3
from BusinessLogic.User import User
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Party import Party
from BusinessLogic.Position import Position
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
            if returnedRow[0] is 0:
                with open('Resources/user_info_complete_with_pass.csv', 'r') as openFile:
                    dataRead = csv.DictReader(openFile)
                    to_db = [(i['user_id'].replace(' ', ''), i['user_program'], i['user_firstName'], i['user_midName'],
                              i['user_lastName'], i['user_email'], i['user_password']) for i in dataRead]

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

    #   WARNING: THIS WILL DROP CURRENT ELECTION TABLE, MAKE SURE TO HANDLE THIS PROPERLY
    def EndElection(self):
        with self.dbConnection:
            #   drop existing table
            self.dbServer.execute("DELETE FROM election_info")

    #   write a start date for the election in the election_info table in the database
    def WriteNewElection(self, newStartDate: datetime, newEndDate: datetime):
        with self.dbConnection:
            #   insert only if election table is empty
            self.dbServer.execute("SELECT COUNT(start_date) FROM election_info")
            if (self.dbServer.fetchone()[0] == 0):
                self.dbServer.execute("INSERT OR REPLACE INTO election_info VALUES(:newStartDate, :newEndDate)",
                                      {'newStartDate':newStartDate.date().strftime("%Y-%m-%d"),
                                       'newEndDate':newEndDate.date().strftime("%Y-%m-%d")})

    #   return user if userId exists in database
    def ReadUser_with_userId(self, userId):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_id = :idToFind", {'idToFind':userId})
        userDetails = self.dbServer.fetchone()
        if userDetails is not None:
            #   userDetails[5] is email, not needed for defining User
            returnUser = User(int(userDetails[0]), userDetails[1], userDetails[2], userDetails[3], userDetails[4],
                              userDetails[6])
            return returnUser
        else:
            return None

    def ReadUser_with_email_and_password(self, email, password):
        self.dbServer.execute("SELECT * FROM user_info WHERE user_email = :emailToFind AND user_password = :passwordKey",
                              {'emailToFind':email, 'passwordKey':password})
        userDetails = self.dbServer.fetchone()
        if userDetails is not None:
            #   userDetails[5] is email, not needed for defining User
            returnUser = User(int(userDetails[0]), userDetails[1], userDetails[2], userDetails[3], userDetails[4],
                              userDetails[6])
            return returnUser
        else:
            return None

    #   returns true if the email exists in the database, otherwise false
    def ReadUser_email_exists(self, email):
        self.dbServer.execute(
            "SELECT * FROM user_info WHERE user_email = :emailToFind", {'emailToFind': email})
        if self.dbServer.fetchone() is None:
            #   no email match found
            return False
        else:
            #   email exists
            return True

    #   return a list of User instances from database
    def ReadUsers(self):
        self.dbServer.execute("SELECT user_id FROM user_info")
        fetchedIds = self.dbServer.fetchall()
        if fetchedIds is not None:
            #   userDetails[5] is email, not needed for defining User
            returnUserList = []
            for fetchedId in fetchedIds:
                returnUserList.append(self.ReadUser_with_userId(fetchedId[0]))
            return returnUserList
        else:
            return None

    #   return candidate if userId exists in database
    def ReadCandidate_with_userId(self, userId):
        returnUser = self.ReadUser_with_userId(userId)
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

    def ReadCandidate_with_email_and_password(self, email, password):
        returnUser = self.ReadUser_with_email_and_password(email, password)
        if returnUser is not None:
            #   get candidate details
            self.dbServer.execute("SELECT * FROM candidate_info WHERE user_id = :idToFind",
                                                     {'idToFind': returnUser.GetUserId()})
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
        #   NOTE: partyName is case-sensitive
        self.dbServer.execute("SELECT user_id FROM candidate_info WHERE candidate_party = :partyNameToFind",
                              {'partyNameToFind': partyName})
        returnCandList = []
        candidateIdReadList = self.dbServer.fetchall()
        for candidateIdRead in candidateIdReadList:
            returnCandList.append(self.ReadCandidate_with_userId(candidateIdRead))

        if len(returnCandList) == 0:
            return None
        else:
            return returnCandList

    #   returns a datetime instance of start date
    def ReadElectionStartDate(self):
        self.dbServer.execute("SELECT start_date FROM election_info")
        electionDetail = self.dbServer.fetchone()

        #   check if no election started yet
        if electionDetail is None:
            return None

        startDate = datetime.strptime(electionDetail[0],"%Y-%m-%d")

        return startDate

#   returns a datetime instance of start date
    def ReadElectionEndDate(self):
        self.dbServer.execute("SELECT end_date FROM election_info")
        electionDetail = self.dbServer.fetchone()

        #   check if no not ended
        if electionDetail is None:
            return None

        startDate = datetime.strptime(electionDetail[0],"%Y-%m-%d")

        return startDate