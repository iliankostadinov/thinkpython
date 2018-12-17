#!/usr/bin/env python3

"""
 Write a function called cumsum that takes a list of numbers and returns
 the cumulative sum; that is, a new list where the ith element is the sum
 of the first i + 1 elements from the original list
"""


def cumsum(t):
    new_t = []
    for i in range(len(t)):
        new_t += [sum(t[:i+1])]
    return new_t


if __name__ == "__main__":
    print(cumsum([1, 2, 3, 4, 5]))
