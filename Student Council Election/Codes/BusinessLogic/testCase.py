from BusinessLogic.Candidate import Candidate
from BusinessLogic.Position import Position
from BusinessLogic.Party import Party
from BusinessLogic.VoteTicket import VoterTicket
from BusinessLogic.Election import Election
from BusinessLogic.UserInterface import UserInterface
from UI.LogIn import Ui_LogIn
from DataAccess.DataAccess import DataAccess
from PyQt5 import QtWidgets
from datetime import datetime
import unittest, sys

class TestCase(unittest.TestCase):
    def test_login_interface_blank_email_and_password(self):
        ui = UserInterface()
        ui.set_user_email_and_password('','')
        self.assertFalse(ui.is_User())

    def test_login_interface_invalid_email_and_blank_password(self):
        ui = UserInterface()
        ui.set_user_email_and_password('lbzmercado', '')
        self.assertFalse(ui.is_User())

    def test_login_interface_invalid_email_and_blank_password_test_for_existence_of_valid_email(self):
        ui = UserInterface()
        ui.set_user_email_and_password('lbzmercado', '')
        self.assertFalse(ui.user_email_is_valid())

    def test_login_interface_valid_email_and_blank_password_test_for_existence_of_valid_email(self):
        ui = UserInterface()
        ui.set_user_email_and_password('lbzmercado@mymail.mapua.edu.ph', '')
        self.assertTrue(ui.user_email_is_valid())

    def test_login_interface_valid_email_and_invalid_password(self):
        ui = UserInterface()
        ui.set_user_email_and_password('lbzmercado@mymail.mapua.edu.ph', '2015102131af')
        self.assertFalse(ui.is_User())

    def test_login_interface_valid_email_and_valid_password(self):
        ui = UserInterface()
        ui.set_user_email_and_password('lbzmercado@mymail.mapua.edu.ph', '2015102131')
        self.assertTrue(ui.is_User())
    #   Business Logic Test 1
    # def testCase1(self):
    #     indepPart = 'Independent'
    #     cand1 = Candidate('2015102131','CPE','Luis Benjamin', 'Zarate', 'Mercado', None,
    #                       Position.PRESIDENT, indepPart)
    #     cand2 = Candidate('2015100194','CPE','Glenn Christian', 'Dela Cruz', 'Sioson', None,
    #                       Position.VICE_PRESIDENT_EXT, indepPart)
    #     cand3 = Candidate('2015105002','CPE','Lauren', 'Castro', 'Tan', None,
    #                       Position.PRESIDENT, indepPart)
    #     cand4 = Candidate('2015110954','CPE','Lemuel Aldwin', 'Pacheco', 'Garcia', None,
    #                       Position.VICE_PRESIDENT_EXT, indepPart)
    #     part1 = Party('NASAGIP')
    #     part2 = Party('PINAMANA')
    #     part1.AddCandidate(cand1)
    #     part1.AddCandidate(cand2)
    #     part2.AddCandidate(cand3)
    #     part2.AddCandidate(cand4)
    #
    #     parties = [part1, part2]
    #     dateStart = datetime(2018,9,29)
    #     dateEnd = datetime(2018,10,10)
    #     db = DataAccess('election_' + ''.join(str(dateStart.date()).split('-')) + '.db')
    #
    #     newElection = Election(dateStart, parties)
    #     newElection.SetEndDate(dateEnd)
    #     tick1 = VoterTicket('2015102131', '2015100194')
    #     tick2 = VoterTicket('2015105002', '2015100194')
    #
    #     newElection.AddVoteTicket(tick1)
    #     newElection.AddVoteTicket(tick2)
    #
    #     count = newElection.GetVotesFor(cand2.GetUserId())
    #     print('Votes for '+ cand2.GetLastName() + ' is ' + str(count))
    #     print('TEST CASE 1 PASSED')
    #
    # #   Data Access Test 1
    # def testCase2(self):
    #     db = DataAccess(':memory:')
    #
    #     part1 = Party('NASAGIP')
    #     part2 = Party('PINAMANA')
    #
    #     cand1 = Candidate('2015102131', 'CPE', 'Luis Benjamin', 'Zarate', 'Mercado', None, Position.PRESIDENT, part1)
    #     cand2 = Candidate('2015100194', 'CPE', 'Glenn Christian', 'Dela Cruz', 'Sioson', None,
    #                       Position.VICE_PRESIDENT_EXT, part1)
    #     cand3 = Candidate('2015105002', 'CPE', 'Lauren', 'Castro', 'Tan', None, Position.PRESIDENT, part2)
    #     cand4 = Candidate('2015110954', 'CPE', 'Lemuel Aldwin', 'Pacheco', 'Garcia', None, Position.VICE_PRESIDENT_EXT, part2)
    #
    #     db.WriteUser(cand1)
    #     db.WriteCandidate(cand1)
    #     db.WriteUser(cand2)
    #     db.WriteCandidate(cand2)
    #     db.WriteUser(cand3)
    #     db.WriteCandidate(cand3)
    #     db.WriteUser(cand4)
    #     db.WriteCandidate(cand4)
    #
    #     print(db.ReadUser_with_userId(cand1.GetUserId()).GetEmail())
    #     print(db.ReadCandidate_with_userId(cand1.GetUserId()).GetPlatform())
    #     print(db.ReadUser_with_userId(cand2.GetUserId()).GetEmail())
    #     print(db.ReadCandidate_with_userId(cand2.GetUserId()).GetPlatform())
    #     print(db.ReadUser_with_userId(cand3.GetUserId()).GetEmail())
    #     print(db.ReadCandidate_with_userId(cand3.GetUserId()).GetPlatform())
    #     print(db.ReadUser_with_userId(cand4.GetUserId()).GetEmail())
    #     print(db.ReadCandidate_with_userId(cand4.GetUserId()).GetPlatform())
    #     print('TEST CASE 2 PASSED')
    #
    # #   Data Access Test 2
    # def testCase3(self):
    #     indepPart = 'Independent'
    #     cand1 = Candidate('2015102131', 'CPE', 'Luis Benjamin', 'Zarate', 'Mercado', None,
    #                       Position.PRESIDENT, indepPart)
    #     cand2 = Candidate('2015100194', 'CPE', 'Glenn Christian', 'Dela Cruz', 'Sioson', None,
    #                       Position.VICE_PRESIDENT_EXT, indepPart)
    #     cand3 = Candidate('2015105002', 'CPE', 'Lauren', 'Castro', 'Tan', None,
    #                       Position.PRESIDENT, indepPart)
    #     cand4 = Candidate('2015110954', 'CPE', 'Lemuel Aldwin', 'Pacheco', 'Garcia', None,
    #                       Position.VICE_PRESIDENT_EXT, indepPart)
    #     part1 = Party('NASAGIP')
    #     part2 = Party('PINAMANA')
    #     part1.AddCandidate(cand1)
    #     part1.AddCandidate(cand2)
    #     part2.AddCandidate(cand3)
    #     part2.AddCandidate(cand4)
    #
    #     cand1.SetParty(part1.GetPartyName())
    #     cand2.SetParty(part1.GetPartyName())
    #     cand3.SetParty(part2.GetPartyName())
    #     cand4.SetParty(part2.GetPartyName())
    #
    #     parties = [part1, part2]
    #     dateStart = datetime(2018, 9, 30)
    #     dateEnd = datetime(2018, 10, 10)
    #
    #     db = DataAccess(':memory:')
    #
    #     newElection = Election(dateStart, parties)
    #     newElection.SetEndDate(dateEnd)
    #     tick1 = VoterTicket('2015102131', '2015100194')
    #     tick2 = VoterTicket('2015105002', '2015100194')
    #     db.WriteNewElection(newElection)
    #
    #     newElection.AddVoteTicket(tick1)
    #     newElection.AddVoteTicket(tick2)
    #
    #     count = newElection.GetVotesFor(cand2.GetUserId())
    #     print('Votes for ' + cand2.GetLastName() + ' is ' + str(count))
    #     print('TEST CASE 3 PASSED')