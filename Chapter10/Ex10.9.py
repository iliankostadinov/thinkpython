#!/usr/bin/env python3

"""
 Write a function that reads the file words.txt and builds a list with one
 element per word. Write two versions of this function, one using the append
 method and the other using the idiom t = t + [x] . Which one takes longer to
 run? Why?
"""


def create_list(filename):
    t = []
    fin = open(filename)
    for line in fin:
        word = line.strip()
        # t = t + [word] // this is very slow
        t.append(word)
    return t


if __name__ == "__main__":
    filename = "../Chapter9/words.txt"
    print(create_list(filename))
