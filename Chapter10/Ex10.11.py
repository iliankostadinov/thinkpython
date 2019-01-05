#!/usr/bin/env python3

"""
 Two words are a "reverse pair" if each is the reverse of the other. Write
 a program that finds all the reverse pairs in the word list.
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


def find_rev_pair():
    fin = open("../Chapter9/words.txt")
    word_list = []
    for words in fin:
        sword = words.strip()
        word_list.append(sword)
    for swords in word_list:
        rword = swords[::-1]
        if in_bisect(word_list, rword):
            print(swords, rword)


find_rev_pair()
