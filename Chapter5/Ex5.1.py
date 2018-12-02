#!/usr/bin/python3

"""
Write a function that reads the current time and converts it to a time of
day in hours, minutes, and seconds, plus the number of days since the epoch
"""

import time


def curDate():
    epochTime = time.time()
    hours = epochTime % (3600 * 24)
    print(hours)


if __name__ == '__main__':

    curDate()
