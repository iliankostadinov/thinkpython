#!/usr/bin/env python3

"""
 Print all palindromic ages between mother and son
"""


if __name__ == "__main__":
    for diff_age in range(17, 41):
        print("For diference in age equals to ", diff_age)
        for son_age in range(0, 100):
            mother_age = son_age + diff_age
            align_son_age = str(son_age).zfill(2)
            align_mother_age = str(mother_age).zfill(2)
            if align_son_age == align_mother_age[::-1]:
                print(align_son_age, align_mother_age)
