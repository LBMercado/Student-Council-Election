from Candidate import Candidate
from Position import Position
from Party import Party
from VoteTicket import VoterTicket
from Election import Election
from datetime import datetime
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
print('End')