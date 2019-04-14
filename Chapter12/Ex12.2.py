#!/usr/bin/env python3

"""
 Write a program that reads a word list from a file and prints all the sets of
 words that are anagrams.
"""

if __name__ == "__main__":
    fin = open("words.txt")
    d = {}
    for words in fin:
        # sort, strip word and store it as a tuple
        key_tup = tuple(sorted(words.strip()))
        # add word to dictionary, where words whit same letters are vaules in
        # same list
        if key_tup not in d:
            d[key_tup] = [words.strip()]
        else:
            d[key_tup].append(words.strip())
    # create list with lenght of d values and d keys
    list_with_elements = []
    tempList = []
    for key in d:
        if len(d[key]) > 1:
            tempLen = len(d[key])
            tempList.append(tempLen)
            tempList.append(key)
            list_with_elements.append(tempList)
            tempList = []
    # sort list_with_elements
    list_with_elements.sort()
    # print longest values in d first
    b = [i[1] for i in reversed(list_with_elements)]
    for k in b:
        print(d[k])
