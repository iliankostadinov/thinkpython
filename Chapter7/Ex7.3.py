#!/usr/bin/env python3

'''
 Write a function called estimate_pi that use formula from Ramanujan
 to compute and return an estimate of pi
 This solution doesn't work may be some day will find why but the
 idea is right
'''

import math


def estimate_pi():
    term = 1
    epsilon = 0.000000000000001
    k = 0
    valOfpi = 0
    while term > epsilon:
        term = (2/9801*math.sqrt(2))*((math.factorial(4*k)*(1103+26390*k))/(math.factorial(k)**4)*(396**(4*k)))
        k += 1
        valOfpi += term
        print(term)
    print(valOfpi)


estimate_pi()
