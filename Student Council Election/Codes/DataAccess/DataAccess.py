#   !/usr/bin/env python

#   import modules
import sqlite3
from BusinessLogic.User import User
from BusinessLogic.Admin import Admin
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Party import Party
from BusinessLogic.Position import Position
from BusinessLogic.VoteTicket import VoteTicket
from BusinessLogic.Voter import Voter
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

            #   THIS IS ESSENTIAL, DO NOT DELETE
            #   user_info reinitialization using file in Resources/user_info_complete_with_pass.csv
            #   don't reinitialize user_info if it is already initialized
            if returnedRow[0] is 0:
                with open('Resources/user_info_complete_with_pass.csv', 'r') as openFile:
                    dataRead = csv.DictReader(openFile)
                    to_db = [(i['user_id'].replace(' ', ''), i['user_program'], i['user_firstName'], i['user_midName'],
                              i['user_lastName'], i['user_email'], i['user_password']) for i in dataRead]

                self.dbServer.executemany('INSERT OR IGNORE INTO user_info VALUES(?,?,?,?,?,?,?)', to_db)

                #   form the emails of the users
                userList = self.ReadAllUsers()
                for user in userList:
                    self.UpdateUser(user)

            #   candidate table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS candidate_info(
                                    user_id INTEGER PRIMARY KEY,
                                    candidate_party TEXT,
                                    candidate_position TEXT,
                                    candidate_platform TEXT,
                                    candidate_path TEXT
                                    )
            """)

            #   reinitialize the candidate_info table
            if returnedRow[0] is 0:
                # initialize the candidates
                self.initialize_candidates_from_preset()

            #   voteTicket table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS vote_ticket(
                                                user_id INTEGER PRIMARY KEY,
                                                REPRESENTATIVE_CSC_id INTEGER,
                                                PRESIDENT_id INTEGER,
                                                VICE_PRESIDENT_INT_id INTEGER,
                                                VICE_PRESIDENT_EXT_id INTEGER,
                                                SECRETARY_EXECUTIVE_ID INTEGER, 
                                                SECRETARY_FINANCE_ID INTEGER,
                                                SECRETARY_AUDIT_ID INTEGER,
                                                SECRETARY_LOGISTICS_ID INTEGER,
                                                SECRETARY_BUDGET_MANAGEMENT_ID INTEGER,
                                                SECRETARY_SCHOLARSHIP_ID INTEGER,
                                                SECRETARY_INFO_CORRESPONDENCE_ID INTEGER,
                                                SECRETARY_AMUSEMENT_RECREATION_ID INTEGER,
                                                SECRETARY_WELFARE_DEV_ID INTEGER,
                                                REPRESENTATIVE_4TH_YEAR_ID INTEGER,
                                                REPRESENTATIVE_3RD_YEAR_ID INTEGER,
                                                REPRESENTATIVE_2ND_YEAR_ID INTEGER,
                                                REPRESENTATIVE_GENERAL_ID INTEGER,
                                                BUSINESS_MANAGER_ID INTEGER
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

            #   THIS IS ESSENTIAL, DO NOT DELETE
            #   user_info reinitialization using file in Resources/user_info_complete_with_pass.csv
            #   don't reinitialize user_info if it is already initialized
            if returnedRow is not None:
                with open('Resources/user_info_complete_with_pass.csv', 'r') as openFile:
                    dataRead = csv.DictReader(openFile)
                    to_db = [(i['user_id'].replace(' ', ''), i['user_program'], i['user_firstName'], i['user_midName'],
                              i['user_lastName'], i['user_email'], i['user_password']) for i in dataRead]
                to_db.pop()  # get that weird last entry off the list
                self.dbServer.executemany('INSERT OR IGNORE INTO user_info VALUES(?,?,?,?,?,?,?)', to_db)

                #   form the emails of the users
                userList = self.ReadAllUsers()
                for user in userList:
                    self.UpdateUser(user)
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS candidate_info(
                                            user_id INTEGER PRIMARY KEY,
                                            candidate_party TEXT,
                                            candidate_position TEXT,
                                            candidate_platform TEXT,
                                            candidate_path TEXT
                                            )
                    """)
            #   voteTicket table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS vote_ticket(
                                                            user_id INTEGER PRIMARY KEY,
                                                            REPRESENTATIVE_CSC_id INTEGER,
                                                            PRESIDENT_id INTEGER,
                                                            VICE_PRESIDENT_INT_id INTEGER,
                                                            VICE_PRESIDENT_EXT_id INTEGER,
                                                            SECRETARY_EXECUTIVE_ID INTEGER, 
                                                            SECRETARY_FINANCE_ID INTEGER,
                                                            SECRETARY_AUDIT_ID INTEGER,
                                                            SECRETARY_LOGISTICS_ID INTEGER,
                                                            SECRETARY_BUDGET_MANAGEMENT_ID INTEGER,
                                                            SECRETARY_SCHOLARSHIP_ID INTEGER,
                                                            SECRETARY_INFO_CORRESPONDENCE_ID INTEGER,
                                                            SECRETARY_AMUSEMENT_RECREATION_ID INTEGER,
                                                            SECRETARY_WELFARE_DEV_ID INTEGER,
                                                            REPRESENTATIVE_4TH_YEAR_ID INTEGER,
                                                            REPRESENTATIVE_3RD_YEAR_ID INTEGER,
                                                            REPRESENTATIVE_2ND_YEAR_ID INTEGER,
                                                            REPRESENTATIVE_GENERAL_ID INTEGER,
                                                            BUSINESS_MANAGER_ID INTEGER
                                                            )
                                    """)
            #   election table
            self.dbServer.execute("""CREATE TABLE IF NOT EXISTS election_info(
                                                                    start_date TEXT,
                                                                    end_date TEXT
                                                                    )
                                            """)

    #   reads csv file from Resources/candidate_info_2018elecs.csv and places them in the database, if not duplicate
    """
    FOLLOW THE FORMAT FOR EACH DATA MEMBER OF A CANDIDATE
    user_id - 10-digit number
    candidate_party - TEXT
    candidate_position - MUST BE ONE OF THE POSITIONS DEFINED IN BusinessLogic/Position.py
    candidate_path - TEXT, refers to the Resources/Candidates/candidate_position/ folder
    """
    def initialize_candidates_from_preset(self):
        candidateInfoFile = 'Resources/candidate_info_2018elecs.csv'

        with open(candidateInfoFile, 'r') as openFile:
            dataRead = csv.DictReader(openFile)
            to_db = [(i['user_id'].replace(' ', ''), i['candidate_party'], i['candidate_position'], i['candidate_platform'],
                      i['candidate_path']) for i in dataRead]

        self.dbServer.executemany('INSERT OR IGNORE INTO candidate_info VALUES(?,?,?,?,?)', to_db)
        self.dbConnection.commit()

    """
    USER CLASS METHODS
    """


    #   return User with matching userId
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

    #   return True if the supplied email and password has a match in the database, otherwise False
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

    #   returns True if the email exists in the database, otherwise False
    def ReadUser_email_exists(self, email):
        self.dbServer.execute(
            "SELECT * FROM user_info WHERE user_email = :emailToFind", {'emailToFind': email})
        if self.dbServer.fetchone() is None:
            #   no email match found
            return False
        else:
            #   email exists
            return True

    #   return a list of User objects, gets every single user stored in the database
    def ReadAllUsers(self):
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

    #   write general class User: Voter, Candidate, Admin
    def WriteUser(self, newUser: User):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO user_info VALUES(?,?,?,?,?,?,?)",
                (newUser.GetUserId(), newUser.GetProgram(), newUser.GetFirstName(),
                    newUser.GetMidName(), newUser.GetLastName(), newUser.GetEmail(),
                    newUser.GetPassword())
                )

    #   update general class User: Voter, Candidate, Admin
    def UpdateUser(self, existingUser: User):
        with self.dbConnection:
            self.dbServer.execute(
                """UPDATE user_info SET user_program = ?, user_firstName = ?, user_midName = ?, 
                user_lastName = ?, user_email = ?, user_password = ? WHERE user_id = ?""",
                (existingUser.GetProgram(), existingUser.GetFirstName(),
                    existingUser.GetMidName(), existingUser.GetLastName(), existingUser.GetEmail(),
                    existingUser.GetPassword(), existingUser.GetUserId())
                )
    #   remove specific class User: Voter, Candidate, Admin
    def RemoveSpecificUser(self, existingUser):
        #   identify specific type of User
        if isinstance(existingUser, (User, Admin)):
            #   remove only from user_info table
            with self.dbConnection:
                self.dbServer.execute("DELETE FROM user_info WHERE user_id = :existingUserId",
                                      {'existingUserId': existingUser.GetUserId()})
        elif isinstance(existingUser, Candidate):
            #   remove from user_info, candidate_info, and vote_ticket tables
            with self.dbConnection:
                self.dbServer.execute("DELETE FROM user_info WHERE user_id = :existingUserId",
                                      {'existingUserId': existingUser.GetUserId()})
                self.dbServer.execute("DELETE FROM candidate_info WHERE user_id = :existingUserId",
                                      {'existingUserId': existingUser.GetUserId()})
                self.dbServer.execute("DELETE FROM vote_ticket WHERE candidate_id = :existingUserId",
                                      {'existingUserId': existingUser.GetUserId()})

        elif isinstance(existingUser, Voter):
            #   remove from user_info, and vote_ticket tables
            with self.dbConnection:
                self.dbServer.execute("DELETE FROM user_info WHERE user_id = :existingUserId",
                                      {'existingUserId': existingUser.GetUserId()})
                self.dbServer.execute("DELETE FROM candidate_info WHERE user_id = :existingUserId",
                                      {'existingUserId': existingUser.GetUserId()})
        else:
            raise TypeError("Unexpected type of parameter existingUser. Received " + (str)(type(existingUser)) + " instead")
    """
    CANDIDATE CLASS METHODS
    """
    #   return Candidate object with matching userId
    def ReadCandidate_with_userId(self, userId):
        returnUser = self.ReadUser_with_userId(userId)
        if returnUser is not None:
            #   get candidate details
            self.dbServer.execute("SELECT * FROM candidate_info WHERE user_id = :idToFind",
                                                     {'idToFind': userId})
            candidateDetails = self.dbServer.fetchone()
            #   check if user is a candidate
            if candidateDetails is not None:
                returnCandidate = Candidate(returnUser.GetUserId(), returnUser.GetProgram(), returnUser.GetFirstName(),
                                            returnUser.GetMidName(),returnUser.GetLastName(),returnUser.GetPassword(),
                                            Position[candidateDetails[2]], candidateDetails[1])
                returnCandidate.SetPlatform(candidateDetails[3])
                returnCandidate.SetPicturePath(candidateDetails[4])
                return returnCandidate
            else:
                return None
        else:
            return None

    #   return Candidate object that matches the given email and password
    def ReadCandidate_with_email_and_password(self, email, password):
        returnUser = self.ReadUser_with_email_and_password(email, password)
        if returnUser is not None:
            #   get candidate details
            self.dbServer.execute("SELECT * FROM candidate_info WHERE user_id = :idToFind",
                                                     {'idToFind': returnUser.GetUserId()})
            candidateDetails = self.dbServer.fetchone()
            #   check if user is a candidate
            if candidateDetails is not None:
                returnCandidate = Candidate(returnUser.GetUserId(), returnUser.GetProgram(), returnUser.GetFirstName(),
                                            returnUser.GetMidName(),returnUser.GetLastName(),returnUser.GetPassword(),
                                            Position[candidateDetails[2]], candidateDetails[1])
                returnCandidate.SetPlatform(candidateDetails[3])
                returnCandidate.SetPicturePath(candidateDetails[4])
                return returnCandidate
            else:
                return None
        else:
            return None

    #   write a new Candidate, use this upon registration of User as Candidate, promote User to Candidate
    def WriteCandidate(self, newCandidate: Candidate):
        with self.dbConnection:
            self.dbServer.execute(
                "INSERT OR IGNORE INTO candidate_info VALUES(?,?,?,?,?)",
                (newCandidate.GetUserId(), newCandidate.GetPartyName(),
                 ((str)(newCandidate.GetPosition())).split('.')[1],
                 newCandidate.GetPlatform(), newCandidate.GetPicturePath())
                                )

    #   demote Candidate back to Voter/User
    def RemoveCandidate(self, candidateId):
        with self.dbConnection:
            self.dbServer.execute("DELETE FROM candidate_info WHERE user_id = :idToFind",
                                  {'idToFind':candidateId})

    """
    VOTER CLASS METHODS
    """

    #   return a list of Voter objects, a User is a Voter if it is not a Candidate
    def ReadAllVoters(self):
        self.dbServer.execute("""SELECT * FROM user_info WHERE NOT EXISTS 
                            (SELECT * FROM candidate_info WHERE user_info.user_id = candidate_info.user_id)
                            AND
                            NOT user_program = 'ADMINISTRATOR'
                            """)
        userDetails = self.dbServer.fetchall()
        if userDetails is not None and len(userDetails) != 0:
            #   userDetails[5] is email, not needed for defining User
            returnVoterList = []
            for voter in userDetails:
                returnVoter = Voter(int(voter[0]), voter[1], voter[2], voter[3], voter[4],
                                    voter[6])
                returnVoterList.append(returnVoter)

                #   get the voteTicket for this Voter, if it exists
                returnVoter.SetVoteTicket(self.ReadVoteTicketWithUserId(voter[0]))

            return returnVoterList
        else:
            return None

    """
    VOTETICKET CLASS METHODS
    """
    #   return a voteTicket object corresponding to the userId
    def ReadVoteTicketWithUserId(self, userId):
        self.dbServer.execute("SELECT * FROM vote_ticket WHERE user_id = :idToFind",
                              {'idToFind': userId})
        voteTickDetails = self.dbServer.fetchone()
        if voteTickDetails is not None:
            returnVoteTicket = VoteTicket(voteTickDetails[0])

            #   skip the first element, it has already been used
            for candId in voteTickDetails[1:]:
                candRead = self.ReadCandidate_with_userId(candId)
                returnVoteTicket.SetPositionWithCandidateId(candRead.GetPosition(), candId)

            return returnVoteTicket
        else:
            return None

    #   return a list of voteTicket objects, reads all what's stored in the database
    def ReadAllVoteTickets(self):
        self.dbServer.execute("SELECT * FROM vote_ticket")
        voteTickDetailsList = self.dbServer.fetchall()
        if voteTickDetailsList is not None:
            returnTickets = []
            #   instantiate each ticket as VoteTicket
            for voteTickDetails in voteTickDetailsList:
                returnVoteTicket = VoteTicket(voteTickDetails[0])
                #   skip the first element, it has already been used
                for candId in voteTickDetails[1:]:
                    candRead = self.ReadCandidate_with_userId(candId)
                    returnVoteTicket.SetPositionWithCandidateId(candRead.GetPosition(), candId)
                returnTickets.append(returnVoteTicket)
            return returnTickets
        else:
            return None

    #   write or update vote ticket of specified voterId into database, if it doesn't exist
    #   voteDict MUST CONTAIN THE FOLLOWING KEYS below
    #   each key must point to a candidateId
    #   abstained votes may be represented by an empty string, or a nonetype
    #   POSITION(key)                   Index(in Enum Position)
    #   REPRESENTATIVE_CSC                = 0
    #   PRESIDENT                         = 1
    #   VICE_PRESIDENT_INT                = 2
    #   VICE_PRESIDENT_EXT                = 3
    #   SECRETARY_EXECUTIVE               = 4
    #   SECRETARY_FINANCE                 = 5
    #   SECRETARY_AUDIT                   = 6
    #   SECRETARY_LOGISTICS               = 7
    #   SECRETARY_BUDGET_MANAGEMENT       = 8
    #   SECRETARY_SCHOLARSHIP             = 9
    #   SECRETARY_INFO_CORRESPONDENCE     = 10
    #   SECRETARY_AMUSEMENT_RECREATION    = 11
    #   SECRETARY_WELFARE_DEV             = 12
    #   REPRESENTATIVE_4TH_YEAR           = 13
    #   REPRESENTATIVE_3RD_YEAR           = 14
    #   REPRESENTATIVE_2ND_YEAR           = 15
    #   REPRESENTATIVE_GENERAL            = 16
    #   BUSINESS_MANAGER                  = 17
    def WriteVoteTicket(self, voterId, voteDict: dict):
        with self.dbConnection:
            self.dbServer.execute("""REPLACE INTO vote_ticket VALUES(
                                                        :voter_id
                                                        :REPRESENTATIVE_CSC,
                                                        :PRESIDENT,
                                                        :VICE_PRESIDENT_INT, 
                                                        :VICE_PRESIDENT_EXT, 
                                                        :SECRETARY_EXECUTIVE, 
                                                        :SECRETARY_FINANCE, 
                                                        :SECRETARY_AUDIT, 
                                                        :SECRETARY_LOGISTICS, 
                                                        :SECRETARY_BUDGET_MANAGEMENT, 
                                                        :SECRETARY_SCHOLARSHIP, 
                                                        :SECRETARY_INFO_CORRESPONDENCE,  
                                                        :SECRETARY_AMUSEMENT_RECREATION, 
                                                        :SECRETARY_WELFARE_DEV,  
                                                        :REPRESENTATIVE_4TH_YEAR, 
                                                        :REPRESENTATIVE_3RD_YEAR, 
                                                        :REPRESENTATIVE_2ND_YEAR,
                                                        :REPRESENTATIVE_GENERAL,
                                                        :BUSINESS_MANAGER
                                                        )
                                """, {
                                'voterId': voterId,
                                'REPRESENTATIVE_CSC':voteDict['REPRESENTATIVE_CSC'],
                                'PRESIDENT':voteDict['PRESIDENT'],
                                'VICE_PRESIDENT_INT':voteDict['VICE_PRESIDENT_INT'],
                                'VICE_PRESIDENT_EXT':voteDict['VICE_PRESIDENT_EXT'],
                                'SECRETARY_EXECUTIVE':voteDict['SECRETARY_EXECUTIVE'],
                                'SECRETARY_FINANCE':voteDict['SECRETARY_FINANCE'],
                                'SECRETARY_AUDIT':voteDict['SECRETARY_AUDIT'],
                                'SECRETARY_LOGISTICS':voteDict['SECRETARY_LOGISTICS'],
                                'SECRETARY_BUDGET_MANAGEMENT':voteDict['SECRETARY_BUDGET_MANAGEMENT'],
                                'SECRETARY_SCHOLARSHIP':voteDict['SECRETARY_SCHOLARSHIP'],
                                'SECRETARY_INFO_CORRESPONDENCE':voteDict['SECRETARY_INFO_CORRESPONDENCE'],
                                'SECRETARY_AMUSEMENT_RECREATION':voteDict['SECRETARY_AMUSEMENT_RECREATION'],
                                'SECRETARY_WELFARE_DEV':voteDict['SECRETARY_WELFARE_DEV'],
                                'REPRESENTATIVE_4TH_YEAR':voteDict['REPRESENTATIVE_4TH_YEAR'],
                                'REPRESENTATIVE_3RD_YEAR':voteDict['REPRESENTATIVE_3RD_YEAR'],
                                'REPRESENTATIVE_2ND_YEAR':voteDict['REPRESENTATIVE_2ND_YEAR'],
                                'REPRESENTATIVE_GENERAL':voteDict['REPRESENTATIVE_GENERAL'],
                                'BUSINESS_MANAGER':voteDict['BUSINESS_MANAGER']
                                }
                                  )

    """
    PARTY CLASS METHODS
    """
    #   return a list of string parties if there are any, otherwise it is an empty list
    def ReadAllPartyNames(self):
        self.dbServer.execute("SELECT DISTINCT candidate_party FROM candidate_info")

        #   reformat since it returns tuples
        returnList = []
        for item in  self.dbServer.fetchall():
            returnList.append(item[0])

        return returnList

    #   return a Candidate object matching the given partyName and position
    def ReadCandidateWithPartyPosition(self, partyName ,position: Position):
        self.dbServer.execute("SELECT user_id FROM candidate_info WHERE "
                              "candidate_party = :partyMatch AND candidate_position = :positionMatch",
                              {'partyMatch':partyName,'positionMatch':position})

    #   return a list of Candidate objects pertaining to a given party name
    def ReadAllPartyCandidates(self, partyName):
        #   NOTE: partyName is case-sensitive
        self.dbServer.execute("SELECT user_id FROM candidate_info WHERE candidate_party = :partyNameToFind",
                              {'partyNameToFind': partyName})
        returnCandList = []
        candidateIdReadList = self.dbServer.fetchall()
        for candidateIdRead in candidateIdReadList:
            returnCandList.append(self.ReadCandidate_with_userId(candidateIdRead[0]))

        if len(returnCandList) == 0:
            return None
        else:
            return returnCandList

    """
    ELECTION CLASS METHODS
    """

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
                                        {'newStartDate': newStartDate.date().strftime("%Y-%m-%d"),
                                        'newEndDate': newEndDate.date().strftime("%Y-%m-%d")})