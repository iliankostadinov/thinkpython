#!/usr/bin/env python3

"""
    Write a module that imports anagram_sets and provides two new functions:
    store_anagrams should store the anagram dictionary in a “shelf”;
    read_anagrams should look up a word and return a list of its anagrams.
"""


import anagram_sets
import dbm
import pickle


def store_anagrams(dictionary):
    db = dbm.open('db_with_anagrams', 'c')
    for k in dictionary:
        db[k] = pickle.dumps(dictionary[k])
    db.close()


def read_anagrams(word):
    db = dbm.open('db_with_anagrams', 'c')
    print(pickle.loads(db[word]))
    db.close()


if __name__ == "__main__":
    # print(anagram_sets.all_anagrams('words.txt'))
    d = anagram_sets.all_anagrams("words.txt")
    store_anagrams(d)
    read_anagrams("opst")
