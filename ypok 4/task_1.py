# Task 1
# The Guessing Game.
# Write a program that generates a random number between 1 and 10
# and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
import random

print("Hello!\nLet's play")
question = int(input("Guess the number from 1 to 10!\n"))
s = random.randint(1, 10)

if question == s:
    print("You winn!!Good Job!!")
else:
    print(f'Wrong! The correct answer was:{s}')
