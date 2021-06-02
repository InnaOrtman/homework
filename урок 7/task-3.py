# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42


def make_operation(operation=str, *arg):
    if operation == '+':
        d = 0
        c = 1
        resalt1 = arg[d] + arg[c]
        if len(arg) <= 2:
            print(resalt1)
        while not c == len(arg) - 1:
            c += 1
            resalt2 = resalt1 + arg[c]
            resalt1 = resalt2
            print(resalt2)
    if operation == '*':
        d = 0
        c = 1
        resalt1 = arg[d] * arg[c]
        if len(arg) <= 2:
            print(resalt1)
        while not c == len(arg) - 1:
            c += 1
            resalt2 = resalt1 * arg[c]
            resalt1 = resalt2
            print(resalt2)
    if operation == '-':
        d = 0
        c = 1
        resalt1 = arg[d] - arg[c]
        if len(arg) >= 1:
            print(resalt1)
        while not c == len(arg) - 1:
            c += 1
            resalt2 = resalt1 - arg[c]
            resalt1 = resalt2
        print(resalt2)


make_operation('+', 7, 7, 2)
make_operation('*', 7, 6)
make_operation('-', 5, 5, -10, -20)

