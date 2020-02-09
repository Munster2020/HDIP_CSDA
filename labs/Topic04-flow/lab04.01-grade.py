# This program reads in
# a students percentage
# and prints out the 
# corresponding grade

percentage = float (input("Enter the percentage: "))
# print (percentage)

if percentage < 0 or percentage > 100:
    # Later we will show you error handling
    # This should really throw an error
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit 1")
elif percentage <= 69.4: # between 60 and 69.4
    print ("Merit 2")
elif percentage >= 69.5: # between 69.5 and 100
    print ("Distinction")