# Task 1
#Write a Python program to detect the number of local variables declared in a function.

def fun():
    x = 1
    name = 'Inna'
    surname = 'Levko'


print(fun.__code__.co_nlocals)
