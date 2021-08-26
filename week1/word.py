#!/usr/bin/env python3

def get_plural(word):

    vowels = ["a", "e", "i", "o", "u"]

    if word[-1] == "x" or word[-1] == "z" or word[-1] == "s" or word[-1] == "o":
        word = word + "es"
    elif word[-2:] == "ch" or word[-2:] == "sh":
        word = word + "es"
    elif word[-1] == "f":
        word = word[:-1] + "ves"
    elif word[-2:] == "fe":
        word = word[:-2] + "ves"
    elif word[-2] not in vowels and word[-1] == "y":
        word = word[:-1] + "ies"
    else:
        word = word + "s"

    return word