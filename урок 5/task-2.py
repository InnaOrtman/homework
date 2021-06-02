# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random
list_1 = []
list_2 = []
list_3 = []
z = 0

while not len(list_1) == 10:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    list_1.append(x)
    list_2.append(y)

common_integers = list(set(list_1).intersection(set(list_2)))
list_3.append(common_integers)

print(list_1, list_2, list_3, sep='\n')





