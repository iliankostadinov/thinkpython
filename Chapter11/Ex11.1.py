#!/usr/bin/env python3

"""
 Write a function that reads the words in words.txt and stores them as
 keys in a dictionary. It doesn't matter what the values are. Then you can
 use the in operator as a fast way to check whether a string is in dictionary
"""


def word_search():
    dictionary = dict()
    fin = open("../Chapter9/words.txt")
    val = 0
    for words in fin:
        val += 1
        swords = words.strip()
        dictionary[swords] = val
    if "aaa" in dictionary:
        print(dictionary["aaa"])


word_search()
