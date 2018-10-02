#!/usr/bin/env python

#import modules
from BusinessLogic.User import User

class Admin(User):
    def __init__(self, firstName, middleName, lastName, password):
        User.__init__(self, 0, 'Administrator', firstName, middleName, lastName, password)

    def IsAdmin(self):
        return True