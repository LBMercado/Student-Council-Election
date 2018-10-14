#   !/usr/bin/env python

#   import modules
from DataAccess.DataAccess import DataAccess
from BusinessLogic.User import User
from BusinessLogic.Admin import Admin
from BusinessLogic.UserInterface import UserInterface, UserNotFound, UserNotYetDefined
from BusinessLogic.Candidate import Candidate

#   this class links the data access layer with the user interface of the application
class AdminInterface(UserInterface):
    def __init__(self, admin: Admin):
        UserInterface.__init__(self)
        self.userDict = {}
        for user in self.data.ReadAllUsers():
            self.userDict[user.GetUserId()]= user
        self.admin = admin
        self.adminCount = 0

        for user in self.userDict.values():
            if user.GetProgram().upper() == 'ADMINISTRATOR':
                self.adminCount += 1

    #   return true if user is in database, otherwise returns false
    def is_User(self):
        #   look into database and find if user exists
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            if self.user.GetUserId() in self.userDict:
                return True
            else:
                return False

    #   return true if user is in database and is an admin, otherwise return false
    def is_Admin(self):
        #   throw an error if user is still null
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   get user info
            if self.user.GetUserId() in self.userDict:
                returnedUser = self.userDict[self.user.GetUserId()]
                self.user = returnedUser
                return self.user.program.upper() == 'ADMINISTRATOR'
            else:
                return False

    #   return true if user is in database and is a candidate, otherwise return false
    def is_Candidate(self):
        #   throw an error if user is still null
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')
        else:
            #   get candidate info
            if self.user.GetUserId() in self.userDict:
                returnedCandidate = self.data.ReadCandidate_with_userId(self.user.GetUserId())
                if returnedCandidate is None:
                    return False
                else:
                    self.user = returnedCandidate
                    return self.user is not None
            else:
                return False

    #   removes the set user if it exists in the database
    def remove_user(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')

        self.data.RemoveSpecificUser(self.user)
        del self.userDict[self.user.GetUserId()]

    #   updates the set user if it exists in the database, otherwise throws an error
    def update_user(self):
        if self.user is None:
            raise UserNotYetDefined('User is not yet defined, cannot proceed to look into database.')

        self.data.UpdateUser(self.user)
        if isinstance(self.user, Candidate):
            self.data.UpdateCandidate(self.user)

    #   adds the set user if it does not exist yet in the database
    def add_user_to_database(self):
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

    def is_user_set(self):
        return self.user is not None

    def set_user_using_userId(self, userId):
        if userId in self.userDict:
            self.user = self.userDict[userId]

    def set_new_user(self, newUser:User):
        if newUser.GetUserId() not in self.userDict:
            self.user = newUser
            self.userDict[newUser.GetUserId()] = newUser
            if self.is_Admin():
                self.adminCount = 0
                for user in self.userDict.values():
                    if user.GetProgram().upper() == 'ADMINISTRATOR':
                        self.adminCount += 1
                #   revert back to User
                self.is_User()

    def set_updated_user(self, updatedUser):
        if updatedUser.GetUserId() in self.userDict:
            self.user = updatedUser
            self.userDict[updatedUser.GetUserId()] = updatedUser
            if self.is_Admin():
                self.adminCount = 0
                for user in self.userDict.values():
                    if user.GetProgram().upper() == 'ADMINISTRATOR':
                        self.adminCount += 1
                #   revert back to User
                self.is_User()

    def reset_user(self):
        self.user = None

    def get_admin_count(self):
        return self.adminCount

    def  is_super_admin(self):
        #   super admin has id = 0
        if self.admin.GetUserId() == 0:
            return True
        else:
            return False