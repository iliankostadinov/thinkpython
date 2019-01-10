#!/usr/bin/env python3

"""
 Read the documentation of dictionary method setdefault and use it to write
 a more concise version of invert_dict.
"""


def invert_dict(d):
    inverse = dict()
    for k in d:
        val = d[k]
        inverse.setdefault(val, []).append(k)
    print(inverse)


pesho = {'a': 1, 'b': 2, 'c': 1, 'd': 1}
print(type(pesho))
print(pesho)
invert_dict(pesho)
