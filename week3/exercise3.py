"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function

import random


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """

    message = "Gizzard numbers please:"

    while True:
        try:
            input_number = int(raw_input(message))
            print("Ye {} .".format(input_number))
            return input_number
        except Exception as e:
            print("Try again ({})".format(e))


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to this guessing game for guessing guessers")
    print("Pick a lower  bound")
    lowerBound = not_number_rejector("Enter a lowerBound:")
    upperBound = not_number_rejector("Enter an  upperBound:")
    while upperBound <= lowerBound:
        print("re-enter the upperBound")
        upperBound = not_number_rejector("Enter an  upperBound:")

    print("Ok then, a number between {} and {}".format(lowerBound, upperBound))
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)

    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False

    while not guessed:
        try:
            guessedNumber = int(raw_input("Guess a  number:"))
            print("You guessed {}".format(guessedNumber),)
            if guessedNumber == actualNumber:
                print("Yeee got it I think, It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, ha if you know what I  mean")
            elif guessedNumber > upperBound:
                print("out of range, try again")
            elif guessedNumber < lowerBound:
                print("out of range, try again")
            else:
                print("too big, you wish")
        except Exception as e:
            print("that is not a number, try again".format(e),)
    return "You got it!"
    pass


if __name__ == "__main__":
    advancedGuessingGame()
