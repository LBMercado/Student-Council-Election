#!/usr/bin/env python

#import modules
import User.py

class Voter(User):
    def __init__(self, id, firstName, middleName, lastName, email):
        User.__init__(self, id, firstName, middleName, lastName, email)
        self.voteTicket = []

    def VoteFor(self, candidate):
        #initialize a voter ticket
        #add voter + candidate details to voter ticket
        #add voter ticket to current election handler
        pass