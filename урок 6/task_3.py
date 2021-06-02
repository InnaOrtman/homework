# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

numbers = [(x, x * x) for x in range(1, 10)]


print(numbers)


