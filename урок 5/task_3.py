# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

import random

list_1 = []
list_2 = []

while not len(list_1) == 100:
    x = random.randint(1, 100)
    list_1.append(x)
    if x % 7 == 0 and x % 5 == 1:
        list_2.append(x)

print(list_1)
print(list_2)




