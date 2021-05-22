# Task 2
# The birthday greeting program.
# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

print("Hello!\nLet's play")
name = input('What is your name?\n').title()
age = int(input("What is your age?\n"))
print(f'Hello {name}, on your next birthday you’ll be {age+1} years')

