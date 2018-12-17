#!/usr/bin/env python3

"""
 If there are 23 students in your class, what are the chances that two of you
 have the same birthday? You can estimate this probability by generating random
 samples of 23 birthdays and checking for matches. Hint: you can generate
 random birthdays with the randint function in the random module.
"""


import random


def gen_bur():
    birthdays = []
    for i in range(23):
        birthdays.append(random.randint(1, 365))
    return birthdays


def has_dup(t):
    sort_t = sorted(t)
    for i in range(len(t)):
        if t[i] == sort_t[i]:
            return True
    return False


if __name__ == "__main__":
    count_true = 0
    for i in range(1000):
        if has_dup(gen_bur()):
            count_true += 1
    print("Probabilyt of two students to have birthday on the same day is ", count_true/1000)
