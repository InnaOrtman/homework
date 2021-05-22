# Task 4
# The math quiz program
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.
import random

x = random.randint(1, 10)
y = random.randint(1, 10)
z = random.randint(1, 10)
expression = x + (y * z)

print(f"🙃🙃🙃Welcome to the Number Guessing Game!🙃🙃🙃\nYou have to guess the right answer!\n !!! {x} + {y} * {z} !!!")
y = int(input("Write the correct answer!\n(write only numbers, please):"))

if y == expression:
    print('You winn!!!')
else:
    print(f"You lose.😭😭 The answer was {expression}")




