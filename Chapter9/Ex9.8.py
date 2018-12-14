#!/usr/bin/env python3

"""
 Recuiremnts can be found in think in python example 9.8
"""


def last_four_pal(number):
    string = str(number)
    new_string = string[2:]
    if new_string[::-1] == new_string:
        return True
    else:
        return False


def last_five_pal(number):
    string = str(number)
    new_string = string[1:]
    if new_string[::-1] == new_string:
        return True
    else:
        return False


def midle_four_pal(number):
    string = str(number)
    new_string = string[1:5]
    if new_string[::-1] == new_string:
        return True
    else:
        return False


def all_six_pal(number):
    string = str(number)
    if string[::-1] == string:
        return True
    else:
        return False


if __name__ == "__main__":
    for i in range(100000, 999997):
        if last_four_pal(i) and last_five_pal(i+1) and midle_four_pal(i+2) and\
           all_six_pal(i+3):
            print(i)
