# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random
list = []

while not len(list) == 10:
    x = random.randint(1, 100)
    list.append(x)
    print(list)

print(f'The maximum value is:{max(list)}')

