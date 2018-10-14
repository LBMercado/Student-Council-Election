from BusinessLogic.Candidate import Candidate
from BusinessLogic.Position import Position
from BusinessLogic.Party import Party
from BusinessLogic.VoteTicket import VoteTicket
from BusinessLogic.Election import Election
from BusinessLogic.UserInterface import UserInterface
from UI.LogIn import Ui_LogIn
from DataAccess.DataAccess import DataAccess
from PyQt5 import QtWidgets
from datetime import datetime
import unittest, sys, os

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

    def test_election_init(self):
        elect = Election.init_with_null_and_dbName('test.db')

    def test_election_function_VerifyVoteTicket_valid_vote_matching_position_and_candidateId(self):
        el = Election.init_with_null_and_dbName('test.db')
        tick = el.GetVoterTicket(2015102131)

        #	valid vote, matching position and candidateId
        tick.SetVote(Position.SECRETARY_EXECUTIVE, 2015104103)
        res = el.VerifyVoteTicket(tick)
        self.assertTrue(res, 'valid vote, matching position and candidateId')
        print('result: ' + str(res))
        tick.ClearVote(Position.SECRETARY_EXECUTIVE)

    def test_election_function_VerifyVoteTicket_invalid_vote_matching_position_only_nonexistent_candidateId(self):
        el = Election.init_with_null_and_dbName('test.db')
        tick = el.GetVoterTicket(2015102131)

        #	invalid vote, matching position only, nonexistent candidateId
        tick.SetVote(Position.SECRETARY_EXECUTIVE, 2015104102)
        res = el.VerifyVoteTicket(tick)
        self.assertFalse(res, 'invalid vote, matching position only, nonexistent candidateId')
        print('result: ' + str(res))
        tick.ClearVote(Position.SECRETARY_EXECUTIVE)

    def test_election_function_VerifyVoteTicket_invalid_vote_matching_candidateId_only(self):
        el = Election.init_with_null_and_dbName('test.db')
        tick = el.GetVoterTicket(2015102131)

        #	invalid vote, matching candidateId only
        tick.SetVote(Position.SECRETARY_WELFARE_DEV, 2015104103)
        res = el.VerifyVoteTicket(tick)
        self.assertFalse(res, 'invalid vote, matching candidateId only')
        print('result: ' + str(res))
        tick.ClearVote(Position.SECRETARY_WELFARE_DEV)

    def test_election_function_VerifyVoteTicket_invalid_vote_no_match_nonexistent_candidateId(self):
        el = Election.init_with_null_and_dbName('test.db')
        tick = el.GetVoterTicket(2015102131)

        #	invalid vote, no match, nonexistent candidateId
        tick.SetVote(Position.SECRETARY_WELFARE_DEV, 2015104102)
        res = el.VerifyVoteTicket(tick)
        self.assertFalse(res, 'invalid vote, no match, nonexistent candidateId')
        print('result: ' + str(res))
        tick.ClearVote(Position.SECRETARY_WELFARE_DEV)

    def test_election_function_VerifyVoteTicket_invalid_vote_candidateId_and_position_mismatch(self):
        el = Election.init_with_null_and_dbName('test.db')
        tick = el.GetVoterTicket(2015102131)

        #	invalid vote, candidateId and position mismatch
        tick.SetVote(Position.REPRESENTATIVE_4TH_YEAR, 2015141516)
        res = el.VerifyVoteTicket(tick)
        self.assertFalse(res,'invalid vote, candidateId and position mismatch')
        print('result: ' + str(res))
        tick.ClearVote(Position.REPRESENTATIVE_4TH_YEAR)

    #   standard name for test dbs = test.db
    def dbCleanup(self):
        os.remove('Database/test.db')

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