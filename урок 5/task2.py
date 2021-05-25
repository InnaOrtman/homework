# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random
list_1 = []
list_2 = []
list_3: list[int] = []
z = 0

while not len(list_1) == 10:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    list_1.append(x)
    list_2.append(y)
    print(list_1)
    print(list_2)
    if list_1[z] == list_2[z]:
        if list_1[z] not in list_3:
            list_3.append(list_1[z])
            z += 1
    else:
        z += 1
# Чесно кажучи, не до кінця зрозуміла суті завдання...зробила як зрозуміла
print(list_3)

