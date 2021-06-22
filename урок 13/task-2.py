# Task 2

# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def test(x):
    def add(y):
        nonlocal x
        return x + y
    return add


function = test(4)
print(function(4))

