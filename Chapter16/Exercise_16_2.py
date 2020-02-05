#!/usr/bin/env python3

"""1. Use the datetime module to write a program that gets the current date and prints the day of
the week.
2. Write a program that takes a birthday as input and prints the user’s age and the number of
days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as the other.
That’s their Double Day. Write a program that takes two birthdays and computes their Double
Day.
4. For a little more challenge, write the more general version that computes the day when one
person is n times older than the other.
"""

import datetime


def print_day_of_week(date):
    d = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    day = datetime.date.weekday(date)
    print(d[day])


if __name__ == "__main__":

    today = datetime.datetime.today()
    print_day_of_week(today)
    birthday = datetime.datetime(1981, 2, 2)

    delta = today - birthday
    age = delta.days // 365

    next_year = today.year + 1
    next_birthday = birthday.replace(next_year)

    delta = next_birthday - today

    print("Your age is %d" % age)
    print("Till next birthday there are:", delta)

    print("For people born on these dates:")
    bday1 = datetime.datetime(day=11, month=5, year=1967)
    bday2 = datetime.datetime(day=11, month=10, year=2003)
    print(bday1)
    print(bday2)

    print("Double Day is")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2 - d1)
    print(dd)
