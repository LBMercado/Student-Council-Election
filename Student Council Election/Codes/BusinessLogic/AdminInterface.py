#   !/usr/bin/env python

#   import modules
from DataAccess.DataAccess import DataAccess
from BusinessLogic.User import User
from BusinessLogic.Admin import Admin
from BusinessLogic.UserInterface import UserInterface, UserNotFound, UserNotYetDefined

#   this class links the data access layer with the user interface of the application
class AdminInterface(UserInterface):
    def __init__(self, admin: Admin):
        UserInterface.__init__(self)
        self.userList = self.data.ReadAllUsers()
        self.user = None
        self.admin = admin

    #   return true if user, otherwise return false
    def is_User(self):
        #   throw an error if user is still null
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   look into database and find if user exists
            #   have to check if user is set using email and password, or student number
            if self.user.GetUserId() is not None:
                returnedUser = self.data.ReadUser_with_userId(self.user.GetUserId())
            else:
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
            #   have to check if user is set using email and password, or student number
            if self.user.GetUserId() is not None:
                returnedUser = self.data.ReadUser_with_userId(self.user.GetUserId())
            else:
                returnedUser = self.data.ReadUser_with_email_and_password(self.user.GetEmail(), self.user.GetPassword())
            if returnedUser is not None:
                self.user = returnedUser
                return self.user.program.upper() == 'ADMINISTRATOR'
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
            #   have to check if user is set using email and password, or student number
            if self.user.GetUserId() is not None:
                returnedCandidate = self.data.ReadCandidate_with_userId(self.user.GetUserId())
            else:
                returnedCandidate = self.data.ReadCandidate_with_email_and_password(self.user.GetEmail(),
                                                                                self.user.GetPassword())
            if returnedCandidate is not None:
                self.user = returnedCandidate
                return True
            else:
                return False

    #   removes the set user if it exists in the database
    def remove_user(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')

        self.data.RemoveSpecificUser(self.user)

    #   updates the set user if it exists in the database, otherwise throws an error
    def update_user(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')

        self.data.UpdateUser(self.user)

    #   adds the set user if it does not exist yet in the database
    def add_user(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')

        self.data.WriteUser(self.user)

    #   returns true if the set user is an admin
    def is_user_admin(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined.')

        #   remember that all admins have the same program: ADMINISTRATOR
        if self.user.GetProgram() == "ADMINISTRATOR":
            return True
        else:
            return False

    def set_user_userId(self, userId):
        self.user = User.init_with_userId(userId)

    def reset_user(self):
        self.user = None