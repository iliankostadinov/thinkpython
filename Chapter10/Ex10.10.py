#!/usr/bin/env python3

"""
 Write a function called in_bisect that takes a sorted list and a target
 value and returns True if the word is in the list and False if it’s not.
"""


def in_bisect(li, value):
    upper_limit = len(li)-1
    lower_limit = 0
    while upper_limit >= lower_limit:
        word_position = (lower_limit + upper_limit)//2
        if li[word_position] == value:
            return True
        if bef_aft(li[word_position], value) == 1:
            lower_limit = word_position+1
        else:
            upper_limit = word_position-1
    return False


def bef_aft(word1, word2):
    tmp_list = []
    tmp_list.append(word1)
    tmp_list.append(word2)
    tmp_list.sort()
    if tmp_list[0] == word1:
        return 1  # if word1 is before word2
    else:
        return 2


if __name__ == '__main__':
    fin = open("../Chapter9/words.txt")
    li = []
    for words in fin:
        swords = words.strip()
        li.append(swords)
    print(in_bisect(li, "aaa"))
