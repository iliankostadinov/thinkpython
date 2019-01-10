#!/usr/bin/env python3

"""
 Write a simpler, faster version of has_duplicates from Ex 10.7
"""


def has_duplicates(l):
    di = {}
    for k in l:
        if di.setdefault(k) is not None:
            return True
        di[k] = k
    return False


if __name__ == "__main__":
    li = [1, 2, 3, 4, 5]
    print(has_duplicates(li))
