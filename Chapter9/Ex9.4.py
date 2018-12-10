#!/usr/bin/env python3

"""
 Write a function named uses_only that takes a word and a string of letters,
 and that returns True if the word contains only letters in the list
"""


def uses_only(word, string):
    for chars in word:
        if chars in string:
            continue
        else:
            return False
    return True
