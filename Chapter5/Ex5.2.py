#!/usr/bin/python3

'''
Check Fermat's theorem
'''


def check_fermat(a, b, c, n):
    if (n > 2) and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def input_numbers():
    print("Please enter numbers whit which you want to check Fermat's theorem")
    a = input()
    b = input()
    c = input()
    n = input()
    check_fermat(int(a), int(b), int(c), int(n))


if __name__ == '__main__':
    input_numbers()
