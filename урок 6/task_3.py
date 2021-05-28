# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

numbers = []

for x in range(10):
    c = x ** 2
    numbers.append(c)

print(numbers)

