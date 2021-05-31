# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42
import abc


def make_operation(operation=str, *arg):
    totalSum = 0
    for number in arg:
        if operation == '+':
            totalSum += number
        elif operation == '-':
            totalSum -= number
        elif operation == '*':
            totalSum = 1
            totalSum *= number
        else:
            print("Invalid input")

    print(totalSum)


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20) # тут спробувала відтворити хронологію прешого кроку і невдало(((
make_operation('*', 7, 6) # те саме...




