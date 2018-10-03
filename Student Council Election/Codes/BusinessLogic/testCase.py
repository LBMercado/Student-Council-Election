from BusinessLogic.Candidate import Candidate
from BusinessLogic.Position import Position
from BusinessLogic.Party import Party
from BusinessLogic.VoteTicket import VoterTicket
from BusinessLogic.Election import Election
from UI.LogIn import Ui_LogIn
from DataAccess.DataAccess import DataAccess
from PyQt5 import QtWidgets
from datetime import datetime
import unittest, sys

class TestCases(unittest.TestCase):
    #   Business Logic Test 1
    def testCase1(self):
        indepPart = 'Independent'
        cand1 = Candidate('2015102131','CPE','Luis Benjamin', 'Zarate', 'Mercado', None,
                          Position.PRESIDENT, indepPart)
        cand2 = Candidate('2015100194','CPE','Glenn Christian', 'Dela Cruz', 'Sioson', None,
                          Position.VICE_PRESIDENT_EXT, indepPart)
        cand3 = Candidate('2015105002','CPE','Lauren', 'Castro', 'Tan', None,
                          Position.PRESIDENT, indepPart)
        cand4 = Candidate('2015110954','CPE','Lemuel Aldwin', 'Pacheco', 'Garcia', None,
                          Position.VICE_PRESIDENT_EXT, indepPart)
        part1 = Party('NASAGIP')
        part2 = Party('PINAMANA')
        part1.AddCandidate(cand1)
        part1.AddCandidate(cand2)
        part2.AddCandidate(cand3)
        part2.AddCandidate(cand4)

        parties = [part1, part2]
        dateStart = datetime(2018,9,29)
        dateEnd = datetime(2018,10,10)
        db = DataAccess('election_' + ''.join(str(dateStart.date()).split('-')) + '.db')

        newElection = Election(dateStart, parties)
        newElection.SetEndDate(dateEnd)
        tick1 = VoterTicket('2015102131', '2015100194')
        tick2 = VoterTicket('2015105002', '2015100194')

        newElection.AddVoteTicket(tick1)
        newElection.AddVoteTicket(tick2)

        count = newElection.GetVotesFor(cand2.GetUserId())
        print('Votes for '+ cand2.GetLastName() + ' is ' + str(count))
        print('TEST CASE 1 PASSED')

    #   Data Access Test 1
    def testCase2(self):
        db = DataAccess(':memory:')

        part1 = Party('NASAGIP')
        part2 = Party('PINAMANA')

        cand1 = Candidate('2015102131', 'CPE', 'Luis Benjamin', 'Zarate', 'Mercado', None, Position.PRESIDENT, part1)
        cand2 = Candidate('2015100194', 'CPE', 'Glenn Christian', 'Dela Cruz', 'Sioson', None,
                          Position.VICE_PRESIDENT_EXT, part1)
        cand3 = Candidate('2015105002', 'CPE', 'Lauren', 'Castro', 'Tan', None, Position.PRESIDENT, part2)
        cand4 = Candidate('2015110954', 'CPE', 'Lemuel Aldwin', 'Pacheco', 'Garcia', None, Position.VICE_PRESIDENT_EXT, part2)

        db.WriteUser(cand1)
        db.WriteCandidate(cand1)
        db.WriteUser(cand2)
        db.WriteCandidate(cand2)
        db.WriteUser(cand3)
        db.WriteCandidate(cand3)
        db.WriteUser(cand4)
        db.WriteCandidate(cand4)

        print(db.ReadUser(cand1.GetUserId()).GetEmail())
        print(db.ReadCandidate(cand1.GetUserId()).GetPlatform())
        print(db.ReadUser(cand2.GetUserId()).GetEmail())
        print(db.ReadCandidate(cand2.GetUserId()).GetPlatform())
        print(db.ReadUser(cand3.GetUserId()).GetEmail())
        print(db.ReadCandidate(cand3.GetUserId()).GetPlatform())
        print(db.ReadUser(cand4.GetUserId()).GetEmail())
        print(db.ReadCandidate(cand4.GetUserId()).GetPlatform())
        print('TEST CASE 2 PASSED')

    #   Data Access Test 2
    def testCase3(self):
        indepPart = 'Independent'
        cand1 = Candidate('2015102131', 'CPE', 'Luis Benjamin', 'Zarate', 'Mercado', None,
                          Position.PRESIDENT, indepPart)
        cand2 = Candidate('2015100194', 'CPE', 'Glenn Christian', 'Dela Cruz', 'Sioson', None,
                          Position.VICE_PRESIDENT_EXT, indepPart)
        cand3 = Candidate('2015105002', 'CPE', 'Lauren', 'Castro', 'Tan', None,
                          Position.PRESIDENT, indepPart)
        cand4 = Candidate('2015110954', 'CPE', 'Lemuel Aldwin', 'Pacheco', 'Garcia', None,
                          Position.VICE_PRESIDENT_EXT, indepPart)
        part1 = Party('NASAGIP')
        part2 = Party('PINAMANA')
        part1.AddCandidate(cand1)
        part1.AddCandidate(cand2)
        part2.AddCandidate(cand3)
        part2.AddCandidate(cand4)

        cand1.SetParty(part1.GetPartyName())
        cand2.SetParty(part1.GetPartyName())
        cand3.SetParty(part2.GetPartyName())
        cand4.SetParty(part2.GetPartyName())

        parties = [part1, part2]
        dateStart = datetime(2018, 9, 30)
        dateEnd = datetime(2018, 10, 10)

        db = DataAccess(':memory:')

        newElection = Election(dateStart, parties)
        newElection.SetEndDate(dateEnd)
        tick1 = VoterTicket('2015102131', '2015100194')
        tick2 = VoterTicket('2015105002', '2015100194')
        db.WriteNewElection(newElection)

        newElection.AddVoteTicket(tick1)
        newElection.AddVoteTicket(tick2)

        count = newElection.GetVotesFor(cand2.GetUserId())
        print('Votes for ' + cand2.GetLastName() + ' is ' + str(count))
        print('TEST CASE 3 PASSED')

    #   Business + Data Access + UI Integration Test 1: Login interface
    def testCase4(self):
        #   load application
        app = QtWidgets.QApplication(sys.argv)
        LogIn = QtWidgets.QWidget()
        ui = Ui_LogIn()
        ui.setupUi(LogIn)

        #   test cases for login:
        print('Test 1: Blank input')
        ui.lineEditUsername.setText('')
        ui.lineEditPassword.setText('')
        print('Username: ' + ui.lineEditUsername.text())
        print('Password: ' + ui.lineEditPassword.text())
        print('Output: ' + ui.labelError.text())
        ui.logIn()

        print('Test 2: Blank email, any password')
        ui.lineEditUsername.setText('')
        ui.lineEditPassword.setText('foobar')
        print('Username: ' + ui.lineEditUsername.text())
        print('Password: ' + ui.lineEditPassword.text())
        print('Output: ' + ui.labelError.text())
        ui.logIn()

        print('Test 3: any email, blank password')
        ui.lineEditUsername.setText('foobar')
        ui.lineEditPassword.setText('')
        print('Username: ' + ui.lineEditUsername.text())
        print('Password: ' + ui.lineEditPassword.text())
        print('Output: ' + ui.labelError.text())
        ui.logIn()

        print('Test 4: any email, any password')
        ui.lineEditUsername.setText('foobar')
        ui.lineEditPassword.setText('helloworld')
        print('Username: ' + ui.lineEditUsername.text())
        print('Password: ' + ui.lineEditPassword.text())
        print('Output: ' + ui.labelError.text())
        ui.logIn()

        print('Test 5: correct email, blank password')
        ui.lineEditUsername.setText('lbzmercado@mymail.mapua.edu.ph')
        ui.lineEditPassword.setText('')
        print('Username: ' + ui.lineEditUsername.text())
        print('Password: ' + ui.lineEditPassword.text())
        print('Output: ' + ui.labelError.text())
        ui.logIn()

        print('Test 6: correct email, correct password')
        ui.lineEditUsername.setText('lbzmercado@mymail.mapua.edu.ph')
        ui.lineEditPassword.setText('2015102131')
        print('Username: ' + ui.lineEditUsername.text())
        print('Password: ' + ui.lineEditPassword.text())
        print('Output: ' + ui.labelError.text())
        ui.logIn()

        LogIn.close()