#!/usr/bin/env python3

"""
 Write a function called in_bisect that takes a sorted list and a target
 value and returns True if the word is in the list and False if it’s not.
"""


def in_bisect(li, value):
    value_sum = word_val(value)
    word_position = int(len(li)/2)
    cur_word_sum = word_val(li[word_position])
    while cur_word_sum != value_sum:
        if value_sum > cur_word_sum:
            word_position = int((len(li)+word_position)/2)
            cur_word_sum = word_val(li[word_position])
        else:
            word_position = int((len(li)-word_position-1)/2)
            cur_word_sum = word_val(li[word_position])
    return word_position


def word_val(word):
    int_value = 0
    for i in word:
        int_value += ord(i)
    return int_value


print(in_bisect(["todor", "ilian", "gosho", "petko"], "ilian"))
