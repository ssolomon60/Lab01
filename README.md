# Guessing Game (Lab 01)

## Description

This program is a simple guessing game written in Python.
The user chooses a maximum number, and the program randomly picks a number between 1 and that value.
The user keeps guessing until they find the correct number.
The program tells the user if their guess is too high or too low and keeps track of all guesses.

---

## How to Run

1. Make sure Python is installed on your computer
2. Open a terminal or command prompt
3. Navigate to the folder where the file is saved
4. Run the program using:

```
python3 Lab01.py
```

---

## How It Works

* The user enters a number to set the range
* The program picks a random number
* The user guesses the number
* The program gives feedback:

  * "Too high!" if the guess is too big
  * "Too low!" if the guess is too small
* The loop continues until the correct number is guessed
* At the end, the program shows:

  * How many guesses it took
  * A list of all guesses

---

## Example

```
Pick a positive integer: 10
Guess a number between 1 and 10
> 5
    Too low!
> 8
    Too high!
> 7
You found it in 3 guesses.
Your guesses were: [5, 8, 7]
```

---

## Notes

* This program uses basic Python concepts like:

  * input/output
  * loops
  * if statements
  * lists
* It was created as part of a beginner programming assignment.
