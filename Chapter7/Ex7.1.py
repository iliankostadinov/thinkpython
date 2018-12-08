#!/usr/bin/env python3

import math

'''
 Write a function called mysqrt that takes parameter a, chooses a reasonable
 value of x, and returns an estimate of the square root of a
'''


def mysqrt(a):
    x = a/2
    epsilon = 0.00000000001
    while True:
        y = (x + a/x)/2
        if abs(y - x) < epsilon:
            break
        x = y
    return x


def test_square_root():
    print("a    mysqrt(a)     math.sqrt(a)   diff")
    print("-    ---------     -------------  ----")
    i = 1
    while i < 10:
        #print(f'vale of {math.pi:.3f}')
        print(f'{i:.1f}  {mysqrt(i):.11f} {math.sqrt(i):.11f}  {abs(mysqrt(i) - math.sqrt(i)):.11}')
        i += 1


test_square_root()
