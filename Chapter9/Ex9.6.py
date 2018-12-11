#!/usr/bin/env python3

"""
 Write a function called is_abecedarian that returns True if the letters in a
 word appear in alphabetical order (double letters are ok). How many
 abecederian words are there?
"""


def is_abecedarian(word):
    tmp_char = 'a'
    for letters in word:
        if tmp_char > letters:
            return False
        tmp_char = letters
    return True


if __name__ == "__main__":
    fin = open("words.txt")
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            count += 1
    print(count)
