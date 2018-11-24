#!/usr/bin/python3

# Whrite a function named right_justify that takes a  string named s as a
# parameter and prints the string with enough leading spaces so that  the
# last letter of the string is in column 70 of the display


def right_justify(s):

    if len(s) > 70:
        print("Lenght of the string should be less then 70 characters")
    elif len(s) == 70:
        print(s)
    else:
        lenghtOfEmptyStr = 69 - len(s)
        emptyStr = ' '
        for i in range(0, lenghtOfEmptyStr):
            emptyStr += ' '
        print(emptyStr+s)


if __name__ == '__main__':

    print("Please enter a string")
    inStr = input()
    right_justify(inStr)
