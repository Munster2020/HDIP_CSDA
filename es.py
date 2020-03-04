# Created by: Brian Shortiss
# Created on: 4 March 2020

# Write a program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line. 

# Sources:
# https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python
# https://www.gutenberg.org/files/2701/old/moby10b.txt
# 

f = open ('moby10b.txt', 'r')
moby = f.read ()
f.close ()

freq = moby.count ('e')
print (freq)