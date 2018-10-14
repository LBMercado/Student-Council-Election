#	!/usr/bin/env python
#	creates an email address using the characters
#	in the first name and middleName, and the entire lastname before
#	concatenating @mymail.mapua.edu.ph

#	import statements
import re

class NameToEmail:
	def __init__(self, firstNameList, midName, lastName):
		#	firstNameList should be a list of strings
		#	midName and lastName should be a string
        #	all inputted strings will be automatically converted to lowercase

		#	remove any special characters other than a-z
		regex = re.compile('[^a-zA-Z]')
		midName = regex.sub('', midName)
		lastName = regex.sub('', lastName)

		self.firstNameList = [fName.lower() for fName in firstNameList]
		self.firstNameList = [regex.sub('', fName) for fName in self.firstNameList]

		self.middleName = midName.lower()
		self.lastName = lastName.lower()
		self.email = None
		
	def ConvertNameToEmail(self, additionalChars = 0):
		#input: additionalChars - this will slowly build up the first name, keep it zero as much as possible
		#the process considers the following:
		#1. The initials of the first and middle names is taken as a letter set
		#2. the last name should be added succeeding the formed letter set in (1)
		#3. the email format @mymail.mapua.edu.ph should follow after (2)
		letterSet = ''

		#	there will always be a first name
		letterSet += self.firstNameList[0][0]
		nameList = self.firstNameList

		#	this first name will be used for the additionalChars algorithm, so remove it
		nameList.remove(self.firstNameList[0])

		if len(self.middleName) != 0:
			nameList.append(self.middleName)

		firstNameIndex = 1

		while (additionalChars > 0 and firstNameIndex <= len(self.firstNameList[0]) - 1):
			letterSet += self.firstNameList[0][firstNameIndex]
			firstNameIndex += 1
			additionalChars -= 1

		for name in nameList:
			letterSet += name[0]

		#form the email
		self.email = letterSet + self.lastName + '@mymail.mapua.edu.ph'
		
	def SetFirstNameList(self, firstNameList):
		#	remove any special characters other than a-z
		regex = re.compile('[^a-zA-Z]')

		self.firstNameList = [fName.lower() for fName in firstNameList]
		self.firstNameList = [regex.sub('', fName) for fName in self.firstNameList]
		
	def SetLastName(self, lastName):
		#	remove any special characters other than a-z
		regex = re.compile('[^a-zA-Z]')
		self.lastName = regex.sub('', lastName)
		self.lastName = self.lastName.lower()

	def SetMidName(self, midName):
		#	remove any special characters other than a-z
		regex = re.compile('[^a-zA-Z]')
		self.middleName = regex.sub('', midName)
		self.middleName = self.middleName.lower()

	def GetEmail(self):
		if (self.email != None):
			return self.email