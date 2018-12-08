#!/usr/bin/env python3

"""
 Write a function called rotate_word that takes a string and an integer as
 parameters, and returns a new string that contains the leter from original
 string rotated by the given amount
"""


def rotate_word(word, number):
    new_word = ''
    for char in word:
        new_char = chr(ord(char) + number)
        temp_word = new_word
        new_word = temp_word + new_char
    return(new_word)



if __name__ == "__main__":
    print(rotate_word("ilian", 3))
