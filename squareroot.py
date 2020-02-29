# Created by: Brian Shortiss
# Created on: 29 February 2020

# Write a program that takes a positive floating-point number as input
# and outputs an approximation of its square root. You should create a
# function called sqrt that does this.

# Sources:
# https://en.wikipedia.org/wiki/Newton%27s_method
# https://www.cs.swarthmore.edu/~grace/cs21/f14/notes/SampleProblems.html
# https://github.com/codevscolor/codevscolor/blob/master/python/find_squareroot.py
# https://stackoverflow.com/questions/8347435/sqrt-takes-exactly-2-arguments-1-given
# https://medium.com/@surajregmi/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64
# https://www.youtube.com/watch?v=tUFzOLDuvaE


# Asks the user to enter a postive floating-point number.

number = float(input("Enter a postive floating-point number to find an approximation of it's square root : "))

# Creates a function to calculate an approximation of 
# it's square root using Newton's Method. Runs Newtons Method
# over and over until we get closest approximation.

def sqrt (num, error=0.00001): # Terminating Condition sets an erro parameter, this can be adjusted
    guess = num # The first guess
    diff = 999999999 
    while diff > error:
        newGuess = guess - ((guess**2 - num) / (2*guess)) # Newton's Method

        diff = newGuess - guess # Could be positive or negative
        if diff < 0: # The if statement flips negative to positive 
            diff *= -1

        guess = newGuess
    return guess
print (sqrt (number))