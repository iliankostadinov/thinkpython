#!/usr/bin/env python3

"""
 Write a function uses_all that takes a word and a string of required letters,
 and that return True if the word uses all the required letters at least once.
 How many words are there that use all the vowels aeiuo? How about aeiouy?
"""


def uses_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True


def count_words(string):
    fin = open('words.txt')
    count = 0
    for line in fin:
        if uses_all(line, string):
            count += 1
    return count


if __name__ == "__main__":
    print(count_words('aeiou'))
    print(count_words('aeiouy'))
