# Task 3
# Words combination
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’,
# so it should print 5 random strings(words) that combine characters
# ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)
import random

name = input("Enter your name:")
list = []
f = 0
for g in name:
    list += g
while f < 5:
 random.shuffle(list)
 print(list[0:len(list)])
 f +=1



