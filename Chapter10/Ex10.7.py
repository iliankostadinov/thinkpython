#!/usr/bin/env python3

"""
 Write a function called has_duplicates that takes a list and returns True,
 if there is any element that appears more that once. It should not modify
 the original list.
"""


def has_duplicates(t):
    sor_t = sorted(t)
    for i in range(len(t)-1):
        if sor_t[i] == sor_t[i+1]:
            return True
    return False


if __name__ == "__main__":
    print(has_duplicates([1, 2, 4, 3, 4]))
