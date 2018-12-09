#!/usr/bin/env python3

"""
 Write a function called has_no_e that return True if the given word doesn't
 have the letter "e" in it

 Modify your program from the previous section to print only the words that
 have no "e" and compute the percentage of the words in the list that have
 no "e"
"""


def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True


if __name__ == "__main__":
    number_of_lines = 0
    number_of_words_has_no_e = 0
    fin = open("words.txt")
    for line in fin:
        number_of_lines += 1
        word = line.strip()
        if has_no_e(word):
            number_of_words_has_no_e += 1
            print(word)
    print(number_of_words_has_no_e/number_of_lines*100, "%")
