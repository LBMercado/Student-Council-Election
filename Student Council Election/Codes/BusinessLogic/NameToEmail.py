# Creates an email address using at most three characters
# in the first name and middleName, and the entire lastname before
# concatenating @mymail.mapua.edu.ph

class NameToEmail:
	def __init__(self, firstNameList, midName, lastName):
		#firstNameList should be a list of strings
		#midName and lastName should be a string
                #all inputted strings will be automatically converted to lowercase
		
		self.firstNameList = [fName.lower() for fName in firstNameList]

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

		firstNameIndex = 0

		firstLetterSet = self.firstNameList[0][0]

		while (additionalChars > 0 and firstNameIndex != len(self.firstNameList[0]) - 1):
			firstLetterSet += self.firstNameList[0][firstNameIndex]
			firstNameIndex += 1
			additionalChars -= 1

		secondLetter = ''
		thirdLetter = ''

		if (len(self.firstNameList) == 1): #check if only one first name
			secondLetter = self.firstNameList[0][1]

		else: #greater than two first names
			secondLetter = self.firstNameList[1][0]

		thirdLetter = self.middleName[0]

		#form the email
		self.email = firstLetterSet + secondLetter + thirdLetter + self.lastName + '@mymail.mapua.edu.ph'
		
	def SetFirstNameList(self, firstNameList):
		self.firstNameList = firstNameList
		
	def SetLastName(self, lastName):
		self.lastName = lastName
		
	def GetEmail(self):
		if (self.email != None):
			return self.email