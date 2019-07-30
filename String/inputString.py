#
# Get data from user (through keyboard) and perform
# simple string operations like - length, split
#

userString = input ('Enter data')

print (len(userString))		# find number of characters in input string

userString += ' newstring'	# string concatenating
print (userString)

splitStrings = userString.split()	# default split character is ' '
print(splitStrings)