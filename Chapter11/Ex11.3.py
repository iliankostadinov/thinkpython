#!/usr/bin/env python3

"""
 Memoize the Ackermann function and see if memoization make it
 possible to evaluate the function with bigger arguments.
"""


cache = {}


def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1, 1)
    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ack(m-1, ack(m, n-1))
        return cache[m, n]


print(ack(3, 4))
print(ack(4, 6))

