#   !/usr/bin/env python

#   import modules
from DataAccess.DataAccess import DataAccess
from BusinessLogic.User import User
from BusinessLogic.Candidate import Candidate
from BusinessLogic.Voter import Voter
from BusinessLogic.Admin import Admin

#   this class links the data access layer with the user interface of the application
class UserInterface():
    def __init__(self):
        self.data = DataAccess()
        self.user = None

    #   return true if user, otherwise return false
    def is_User(self):
        #   throw an error if user is still null
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   look into database and find if user exists
            returnedUser = self.data.ReadUser_with_email_and_password(self.user.GetEmail(), self.user.GetPassword())
            if returnedUser is not None:
                self.user = returnedUser
                return True
            else:
                return False

    #   return true if admin, otherwise return false
    def is_Admin(self):
        #   throw an error if user is still null
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   get user info
            returnedUser = self.data.ReadUser_with_email_and_password(self.user.GetEmail(), self.user.GetPassword())
            if returnedUser is not None:
                self.user = returnedUser
                if self.user.program.upper() == 'ADMINISTRATOR':
                    self.user = Admin.morph_user_to_admin(self.user)
                    return True
                else:
                    return False
            else:
                raise UserNotFound('User was not found in the database. '
                                   'Try to call the \"is_User\" function first before calling this one.')

    #   return true if candidate, otherwise return false
    def is_Candidate(self):
        #   throw an error if user is still null
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   get candidate info
            returnedCandidate = self.data.ReadCandidate_with_email_and_password(self.user.GetEmail(),
                                                                                self.user.GetPassword())
            if returnedCandidate is not None:
                self.user = returnedCandidate
                return True
            else:
                return False

    #   return true if candidate, otherwise return false
    def is_Voter(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        if not self.is_Candidate() or not self.is_Admin():
            self.user = Voter.morph_user_to_voter(self.user)
            return True
        else:
            return False

    #   loads the vote tickets provided set User is only a User
    def load_vote_tickets(self):
        if (not self.is_Candidate() or not self.is_Admin()):
            pass

    def user_email_is_valid(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   look into database and find if user exists
            return self.data.ReadUser_email_exists(self.user.GetEmail())

    def set_user_email_and_password(self, email, password):
        self.user = User.init_with_email_and_password(email, password)

    def GetUser(self):
        return self.user

    #   updates user password from database
    def UpdateUser(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   look into database and find if user exists
            self.data.UpdateUser(self.user)

#
#   User defined exceptions for easy debugging
#
class UserNotYetDefined(Exception):
    def __init__(self, message):
        super(UserNotYetDefined, self).__init__(message)

class UserNotFound(Exception):
    def __init__(self, message):
        super(UserNotFound, self).__init__(message)