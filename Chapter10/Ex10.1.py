#!/usr/bin/env python3

"""
 Write a function called nested_sum that takes a list of lists of integers
 and adds up the elements from all of the nested lists.
"""


def nested_sum(t):
    total_sum = 0
    for i in t:
        total_sum += sum(i)
    return total_sum


if __name__ == "__main__":
    li = [[1], [2, 3], [4, 5, 6], [7]]
    print(nested_sum(li))
