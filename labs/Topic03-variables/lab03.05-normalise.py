# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case
# this program also outputs the length of the original string
# and the normalised one

rawString = input ("please enter a string:")
normalisedString = rawString.strip () .lower()

lengthOfRawString = len (rawString)
lengthOfNormalised = len (normalisedString)

print ("That String normalised is : {}".format (normalisedString))
print ("we reduced the input string from {} to {} characters:".format (lengthOfRawString, lengthOfNormalised ))