#!/usr/bin/env python3

'''
 Write a function called gcd that takes parameters a and b and returns
 their greatest common divisor
'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(12, 8))
