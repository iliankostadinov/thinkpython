#!/usr/bin/env python3

'''
 Write a function called is_power that takes parameters a and b and returns
 True if a is a power of b
'''


def is_power(a, b):
    if a/b == 1:
        return True
    if a/b < 1:
        return False
    return is_power(a/b, b)


print(is_power(16, 4))
