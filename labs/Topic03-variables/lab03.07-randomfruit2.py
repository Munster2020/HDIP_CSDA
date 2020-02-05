#This program prints out a random fruit

import random

tup1 = 'Apple', 'Orange', 'Banana', 'Pear'

# We want a random number between 0 and length -1

index = random.randint (0, len (tup1) -1)

tup1 = tup1 [index]

print ("A Random Fruit: {}" .format (tup1))