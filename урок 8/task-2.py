# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def function():
    a = int(input('Enter the number, please:'))
    b = int(input('Enter the number, please:'))
    z = a ** 2 / b
    print(round(z))


try:
    function()
except ValueError as error:
    print('the number is not digit...')
except ZeroDivisionError as error:
    print('You cannot divide by zero, please enter another number')


