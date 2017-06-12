# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
import math
import requests


def countdown(message, start, stop, completion_message):
    """Return a list of countdown messages."""
    messageList = []
    if start < stop:
        step = 1
    else:
        step = -1

    while start != stop:
        message = '{} {}'.format(message, start)
        messageList.append(message)
        start = start + step

    messageList.append(completion_message)
    return messageList


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Calculate hypotenuse of triangle."""
    hyp = math.sqrt(base**2 + height**2)
    return hyp


def calculate_area(base, height):
    """Calculate area of triangle."""
    area = (base*height)/2
    return area


def calculate_perimeter(base, height):
    """Calculate perimeter of triangle."""
    perimeter = base + height + calculate_hypotenuse(base, height)
    return perimeter


def calculate_aspect(base, height):
    """Determine aspect of triangle based on base and height."""
    if height > base:
        aspect = 'tall'
    elif height < base:
        aspect = 'wide'
    elif height == base:
        aspect = 'equal'

    return aspect


def get_triangle_facts(base, height, units="mm"):
    """Collect facts about triangle and return in a dictionary."""
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


def tell_me_about_this_right_triangle(facts_dictionary):
    """Return diagrammatic information with facts."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""

    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)

    if facts_dictionary['aspect'] == "tall":
        tall_info = tall.format(**facts_dictionary)
        return (tall_info + facts)
    elif facts_dictionary['aspect'] == "wide":
        wide_info = wide.format(**facts_dictionary)
        return (wide_info + facts)
    else:
        equal_info = equal.format(**facts_dictionary)
        return (equal_info + facts)


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Return details of triangle based on what is requested."""
    dictionary = get_triangle_facts(base, height)
    if return_diagram and return_dictionary:
        return {'diagram': tell_me_about_this_right_triangle(dictionary),
                'facts': dictionary}
    elif return_diagram:
        return (tell_me_about_this_right_triangle(dictionary))
    elif return_dictionary:
        return {'facts': dictionary}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Create a list of words which increase in length then decrease."""
    pyramid_list = list_of_words_with_lengths(range(3, 21, 2))
    pyramid_list2 = list_of_words_with_lengths(range(20, 3, -2))
    return (pyramid_list + pyramid_list2)


def get_a_word_of_length_n(length):
    """Get word of specfic length from URL."""
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    if length >= 3 and isinstance(length, int):
        try:
            r = requests.get(baseURL + str(length)).text
            return r
        except Exception:
            pass


def list_of_words_with_lengths(list_of_lengths):
    """Create a list of words of length specfied from URL."""
    wordList = []
    for length in list_of_lengths:
        word = get_a_word_of_length_n(length)
        wordList.append(word)
    return wordList


if __name__ == "__main__":
    print ("hi")
