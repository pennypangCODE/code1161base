"""Week 3, Exercise 3.
Steps on the way to making your own guessing game.
"""

from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector

import random


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
    print("\nWelcome to Guessing Game")
    lowerBound = not_number_rejector("Enter a lower bound:")
    print("Now enter the upper bound:")
    upperBound = not_number_rejector("Enter an upper bound:")
    while upperBound <= lowerBound:
        print("re-enter upper bound")
        upperBound = not_number_rejector("Enter an upper bound:")
    pass
    print("then enter a number between {} and {}?".format(lowerBound,
                                                          upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNo = random.randint(lowerBound, upperBound)
    guessed = False

    while not guessed:
        try:
            guessedNo = int(raw_input("guess a number:"))
            print("you guessed {},".format(guessedNo),)
            if guessedNo == actualNo:
                print("you got it! it was {}".format(actualNo))
                guessed = True
            elif guessedNo < lowerBound:
                print("out of range")
            elif guessedNo > upperBound:
                print("out of range")
            elif guessedNo < actualNo:
                print("too small, try again...")
            else:
                print("too big, try again...")
        except Exception as e:
            print("that is not a number...try again".format(e))
    return "You got it!"
    pass


if __name__ == "__main__":
    advancedGuessingGame()
