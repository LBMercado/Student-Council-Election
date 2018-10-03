#	!/usr/bin/env python
#	creates an email address using at most three characters
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
		#1. The first three letters of the email are the first letter of the two first names
		#  then the first letter of the middle name
		#  For cases where the first name is only one, the first two letters of the first name will be taken
		#2. the last name should be added succeeding the three letters in (1)
		#3. the email format @mymail.mapua.edu.ph should follow after (2)
		firstLetterSet = ''
		secondLetter = ''
		thirdLetter = ''

		if len(self.middleName) != 0: #	set third letter only if middle name exists
			thirdLetter = self.middleName[0]
		else:
			additionalChars += 1

		firstNameIndex = 1
		firstLetterSet = self.firstNameList[0][0]

		while (additionalChars > 0 and firstNameIndex <= len(self.firstNameList[0]) - 1):
			firstLetterSet += self.firstNameList[0][firstNameIndex]
			firstNameIndex += 1
			additionalChars -= 1

		if len(self.firstNameList) == 1: #	check if only one first name
			secondLetter = self.firstNameList[0][1]

		else: #	greater than or equal to two first names
			secondLetter = self.firstNameList[1][0]


		#form the email
		self.email = firstLetterSet + secondLetter + thirdLetter + self.lastName + '@mymail.mapua.edu.ph'
		
	def SetFirstNameList(self, firstNameList):
		#	remove any special characters other than a-z
		regex = re.compile('[^a-zA-Z]')

		self.firstNameList = [fName.lower() for fName in firstNameList]
		self.firstNameList = [regex.sub('', fName) for fName in self.firstNameList]
		
	def SetLastName(self, lastName):
		#	remove any special characters other than a-z
		regex = re.compile('[^a-zA-Z]')
		self.lastName = regex.sub('', lastName)

	def SetMidName(self, midName):
		#	remove any special characters other than a-z
		regex = re.compile('[^a-zA-Z]')
		self.middleName = regex.sub('', midName)

	def GetEmail(self):
		if (self.email != None):
			return self.email