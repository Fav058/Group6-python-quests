# Author: Musaedi
# Quest 25: The Number Wizard
# Concept: while loop + if/elif/else — guessing game that tells you
# whether each guess is too high or too low.

import random

secret_number = random.randint(1, 100)  # the computer picks a secret number
guess = None                             # start with no guess yet

print("The Number Wizard has chosen a number between 1 and 100.")
print("Can you guess it?\n")

# Keep looping until the guess matches the secret number.
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Aim higher.")
    elif guess > secret_number:
        print("Too high! Aim lower.")
    else:
        print(f"Correct! The number was {secret_number}. You are a true Number Wizard!")
