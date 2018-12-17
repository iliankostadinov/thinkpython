#!/usr/bin/env python3

"""
 Write a function called chop that takes a list, modifies it by removing
 the first and the last elements, and returns None
"""


def chop(t):
    t.pop(-1)
    t.pop()


if __name__ == "__main__":
    li = [1, 2, 3, 4]
    print(li)
    chop(li)
    print(li)
