from BusinessLogic.Candidate import Candidate
from BusinessLogic.Position import Position
from BusinessLogic.Party import Party
from BusinessLogic.VoteTicket import VoterTicket
from BusinessLogic.Election import Election
from DataAccess.DataAccess import DataAccess
from datetime import datetime
import unittest

class TestCases(unittest.TestCase):
    #   Business Logic Test 1
    def testCase1(self):
        cand1 = Candidate('2015102131','CPE','Luis Benjamin', 'Zarate', 'Mercado', None, Position.PRESIDENT)
        cand2 = Candidate('2015100194','CPE','Glenn Christian', 'Dela Cruz', 'Sioson', None, Position.VICE_PRESIDENT_EXT)
        cand3 = Candidate('2015105002','CPE','Lauren', 'Castro', 'Tan', None, Position.PRESIDENT)
        cand4 = Candidate('2015110954','CPE','Lemuel Aldwin', 'Pacheco', 'Garcia', None, Position.VICE_PRESIDENT_EXT)
        part1 = Party('NASAGIP')
        part2 = Party('PINAMANA')
        part1.AddCandidate(cand1)
        part1.AddCandidate(cand2)
        part2.AddCandidate(cand3)
        part2.AddCandidate(cand4)

        parties = [part1, part2]
        dateStart = datetime(2018,9,30)
        dateEnd = datetime(2018,10,10)

        newElection = Election(dateStart, parties)
        newElection.SetEndDate(dateEnd)
        tick1 = VoterTicket('2015102131', '2015100194')
        tick2 = VoterTicket('2015105002', '2015100194')

        newElection.AddVoteTicket(tick1)
        newElection.AddVoteTicket(tick2)

        count = newElection.GetVotesFor(cand2.userId)
        print(count)
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

        print(db.ReadUser(cand1.GetUserId()))
        print(db.ReadCandidate(cand1.GetUserId()))
        print(db.ReadUser(cand2.GetUserId()))
        print(db.ReadCandidate(cand2.GetUserId()))
        print(db.ReadUser(cand3.GetUserId()))
        print(db.ReadCandidate(cand3.GetUserId()))
        print(db.ReadUser(cand4.GetUserId()))
        print(db.ReadCandidate(cand4.GetUserId()))