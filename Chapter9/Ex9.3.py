#!/usr/bin/env python3

"""
 Write a function named avoids that takes a word and a string of forbidden
 letters and then returns True if the word doesn't use any of the forbidden
 letters.
"""


def avoids(word, string):
    for chars in string:
        if chars in word:
            return False
    return True


if __name__ == "__main__":
    fin = open('words.txt')
    string = input("Please enter letters which shouldn't present\n")
    word_count = 0  # number of words which doesn't contain letters from string
    for line in fin:
        word = line.strip()
        if avoids(word, string):
            word_count += 1
    print("Count of words that doesn't contain this letters is ", word_count)
