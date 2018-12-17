#!/usr/bin/env python3

"""
 Write function called is_sorted that takes a list as a parameter and returns
 True if the list is sorted in ascending order and False otherwise.
"""


def is_sorted(t):
    new_t = []
    for i in t:
        new_t += [i]
    new_t.sort()
    for i in range(len(t)):
        if t[i] != new_t[i]:
            return False
    return True


if __name__ == "__main__":
    print(is_sorted(['b', 'a']))
