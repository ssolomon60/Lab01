# 1. Name:
#      Sydney Solomon
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      This program is a simple guessing game. The user picks a maximum number,
#      and the program randomly selects a number between 1 and that value.
#      The user keeps guessing until they find the correct number.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was understanding how the while loop keeps
#      running until the correct number is guessed. I also had to understand
#      how to save each guess in a list and display it at the end.
# 5. How long did it take for you to complete the assignment?
#      About 1 to 1.5 hours.

import random

print('This is the "guess a number" game.')
print("You try to guess a random number in the smallest number of attempts.")
print()

max_number = int(input("Pick a positive integer: "))

secret = random.randint(1, max_number)

print("Guess a number between 1 and", max_number)

guess = 0
guesses = []

while guess != secret:
    guess = int(input("> "))
    guesses.append(guess)

    if guess > secret:
        print("\tToo high!")
    elif guess < secret:
        print("\tToo low!")

print("You were able to find the number in", len(guesses), "guesses.")
print("The numbers you guessed were:", guesses)