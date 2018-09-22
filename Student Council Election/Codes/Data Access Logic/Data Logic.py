import sqlite3
import os

#to follow nalang yung UPDATE
from pathlib import Path
dirname = "D:/Documents/COE125/Data Logic"
filename = "MainDB"
suffix = ".db"
Path(dirname).joinpath(filename).with_suffix(suffix)
os.path.join('D:/Documents/COE125/Data Logic/Main.db')

connection = sqlite3.connect('Main.db')
dl = connection.cursor()



#var dec
#admin variables        
_admin_firstname = None
_admin_lastname = None
_admin_id = 0
_admin_email = None
_admin_password = None

#candidate variables
_candidate_name = None 
_candidate_id = 0
_candidate_party = None
_candidate_position = None
_candidate_platform = None

#voter slip?
_election_startdate = None
_election_enddate = None
_election_voter = None
_election_position1 = None
_election_position2 = None

#ewan ko sa inyo
_party_candidate1 = None
_party_candidate2 = None

#voter info/student to ah
_user_firstname = None
_user_middlename = None
_user_lastname = None
_user_id = 0
_user_email = None
_user_password = None
#end my life pls





#write
#register sa admin
def write_admin(_admin_firstname,_admin_lastname,_admin_id,_admin_email,_admin_password):
    dl.execute("INSERT INTO admin_info values(?,?,?,?,?)",(_admin_firstname,_admin_lastname,_admin_id,_admin_email,_admin_password))
    dl.execute("COMMIT")
#register sa candidate
def write_candidate(_candidate_name,_candidate_id,_candidate_party,_candidate_position,_candidate_platform):
    dl.execute("INSERT INTO candidate_info values(?,?,?,?,?)",(_candidate_name,_candidate_id,_candidate_party,_candidate_position,_candidate_platform))
    dl.execute("COMMIT")
    
#pag lagay ng mga binoto
def write_election(_election_startdate,_election_enddate,_election_voter,_election_position1,_election_position2):
    dl.execute("INSERT INTO vote_tally values(?,?,?,?,?)",(_election_startdate,_election_enddate,_election_voter,_election_position1,_election_position2))
    dl.execute("COMMIT")

#party party
def write_party(_party_candidate1,_party_candidate2):
    dl.execute("INSERT INTO voter_info values(?,?)",(_party_candidate1,_party_candidate2))
    dl.execute("COMMIT")

#register user
def write_user(_user_firstname,_user_middlename,_user_lastname,_user_id,user_email,user_password):
    dl.execute("INSERT INTO admin_info values(?,?,?,?,?)",(_user_firstname,_user_middlename,_user_lastname,_user_id,user_email,user_password))
    dl.execute("COMMIT")


#read
#to sa login admin
def read_admin(_admin_email,_admin_password):
    dl.execute("SELECT * FROM admin_info WHERE admin_email = ? AND admin_password = ?",(_admin_email,_admin_password)) 
    if dl.fetchone() is not None:
        print ("YES NAKA LOGIN KA NA!!!!")
    else:
        print ("sad")
        
#para sa login voter
def read_user(_user_email,_user_password):
    dl.execute("SELECT * FROM voter_info WHERE voter_email = ? AND voter_password = ?",(_user_email,_user_password)) 
    if dl.fetchone() is not None:
        print ("YES NAKA LOGIN KA NA!!!!")
    else:
        print ("sad")

#def tally_vote()#position , kung sino binoto, ???
#to follow antok na ko

#to pag call gamitin nyo gusto nyo
"""
write_admin(_admin_firstname,_admin_lastname,_admin_id,_admin_email,_admin_password)
write_candidate(_candidate_name,_candidate_id,_candidate_party,_candidate_position,_candidate_platform)
write_election(_election_startdate,_election_enddate,_election_voter,_election_position1,_election_position2)
write_party(_party_candidate1,_party_candidate2)
write_user(_user_firstname,_user_middlename,_user_lastname,_user_id,_user_email,_user_password)

read_admin(_admin_email,_admin_password)
read_user(_user_email,_user_password)

"""