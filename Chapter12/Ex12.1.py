#!/usr/bin/env python3

"""
 Write a function called most_frequent that takes a string and prints
 the letters in decreasing order of frequency.
"""


def most_frequent(s):
    # enter characters in dict as val and key how many times they are met
    d = {}
    for k in s:
        val = d.setdefault(k)
        if val is None:
            d[k] = 1
        else:
            d[k] = val + 1
    # inverse it, so kyes are how many times they are met and val are characters
    inverse_d = {}
    for key in d:
        val = d[key]
        if val not in inverse_d:
            inverse_d[val] = [key]
        else:
            inverse_d[val].append(key)
    # sort kyes and enter them in list
    li = []
    for i in sorted(inverse_d):
        li.append(i)
    # print inveerst frequence of characters
    for i in reversed(li):
        print(inverse_d[i])


most_frequent("mamaiklvmmm")
