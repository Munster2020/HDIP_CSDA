# Write a program that asks a user to input 
# a string and outputs every second letter in reverse order.

sentence = (input("Enter a string : "))

sentence = sentence [::-1]

print ("Heres is you're string reversed and every second letter is:", sentence[::2])
