#!/usr/bin/env python3

"""Write a function called mul_time that takes a Time object and a number and returns
a new Time object that contains the product of the original Time and the number.
Then use mul_time to write a function that takes a Time object that represents the finishing time
in a race, and a number that represents the distance, and returns a Time object that represents the
average pace (time per mile).
"""


class Time:
    """Represent time
    attributes: hour, minute, second
    """


def time_to_int(time):
    minutes = time.hour*60 + time.minute
    seconds = minutes*60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def mul_time(time, number):
    seconds = time_to_int(time)
    product = seconds*number
    return int_to_time(product)


def average_pace(time, distance):
    return mul_time(time, 1/distance)
