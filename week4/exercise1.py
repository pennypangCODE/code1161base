"""All about IO."""
from __future__ import division
from __future__ import print_function
import json
import os
import requests

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)


def success_is_relative():
    """Read from a file.

    Read the success message from week 1, but from here, using a relative path.
    TIP: remember that it's relative to your excecution context, not this file.
         The tests are run from the code1161base directory, that's the
         excecution context for this test.
    TIP: check that there ins't unwanted whitespace or line endings in the
         response. Look into .strip() and see what it does.
    """
    f = open("week1/pySuccessMessage.json", "r")
    return(f.read().strip())
    f.close()


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()

    data = json.loads(json_data)
    path = data["results"][0]

    postcode = path["location"]["postcode"]
    ID = path["id"]["value"]

    return {"lastName":       path["name"]["last"],
            "password":       path["login"]["password"],
            "postcodePlusID": int(postcode) + int(ID)
            }


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here: http://www.setgetgo.com/randomword/
    The only argument that the generator takes is the length of the word.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep", 3
    "dwine", 5
    "tenoner", 7
    "ectomeric", 9
    "archmonarch", 11
    "phlebenterism", 13
    "autonephrotoxin", 15
    "redifferentiation", 17
    "phytosociologically", 19
    "theologicohistorical", 20
    "supersesquitertial", 18
    "phosphomolybdate", 16
    "spermatophoral", 14
    "storiologist", 12
    "concretion", 10
    "geoblast", 8
    "Nereis", 6
    "Leto", 4
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. ?len=
    """
    url = "http://www.setgetgo.com/randomword/get.php?len="
    pyramid = []
    lengthWord = 3
    while lengthWord < 20:
        res = requests.get(url + str(lengthWord)).text
        pyramid.append(str(res))
        lengthWord += 2

    lengthWord = 20
    while lengthWord >= 4:
        res = requests.get(url + str(lengthWord)).text
        pyramid.append(str(res))
        lengthWord -= 2

    return pyramid


def wunderground():
    """Find the weather station for Sydney.

    Get some json from a request parse it and extract values.
    Sign up to https://www.wunderground.com/weather/api/ and get an API key
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    base = "http://api.wunderground.com/api/"
    api_key = "2f3ab1a5d1c0f62a"
    country = "AU"
    city = "Sydney"
    template = "{base}/{key}/conditions/q/{country}/{city}.json"
    url = template.format(base=base, key=api_key, country=country, city=city)
    r = requests.get(url)
    the_json = json.loads(r.text)
    obs = the_json["current_observation"]

    return {"state":           obs["display_location"]["state"],
            "latitude":        obs["observation_location"]["latitude"],
            "longitude":       obs["observation_location"]["longitude"],
            "local_tz_offset": obs["local_tz_offset"]}


def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew'
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    """
    f = open("week4/Trispokedovetiles(laser).gcode", "r").read()
    count = str(f.count("M10 P1"))
    f2 = open("week4/lasers.pew", "w").write(count)
    f.close()
    f2.close()


if __name__ == "__main__":
    print([len(w) for w in wordy_pyramid()])
    print(get_some_details())
    print(wunderground())
    print(diarist())
