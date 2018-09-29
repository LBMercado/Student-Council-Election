#!/usr/bin/env python

#import modules
from User import User

class Admin(User):
    def __init__(self, userId, program, firstName, middleName, lastName, password):
        User.__init__(self, userId, program, firstName, middleName, lastName, password)

    def IsAdmin(self):
        return True