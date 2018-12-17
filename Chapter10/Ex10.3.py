#!/usr/bin/env python3

"""
 Write a function called middle that takes a list and returns a new list
 that contins all but the first and last elements.
"""


def middle(t):
    return t[1:-1]


if __name__ == "__main__":
    li = [1, 2, 3, 4]
    print(middle(li))
    print(li)
