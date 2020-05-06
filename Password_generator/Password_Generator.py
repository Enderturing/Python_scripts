#!/usr/bin/env python

"""Automatic pasword generator defined by lenght, GoloR"""

import random

def GenPass(length):
    ps = str()
    to_choose = "abcdefghijklmnrstopquvwyxz" + "0123456789"
    for i in range(length):
        ps = ps + random.choice(to_choose)
    return(ps)



length = False

while not length:
        userGuess = eval(input("Select your password length: "))
        if userGuess > 10:
            print("Too large to remember, be realistic")
        elif userGuess < 5:
            print("Too short, insecure paswoord")
        else:
            print ("Perfect!")
            length = True
            print("Your new password: " + GenPass(int(userGuess)))

print("Thanks for using, have a nice day")
