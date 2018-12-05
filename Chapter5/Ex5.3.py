#!/usr/bin/python3

# Check if entered numbers can make a triangle


def is_triangle(a, b, c):
    if int(a) > int(b) + int(c):
        print("No")
    elif int(b) > int(a) + int(c):
        print("No")
    elif int(c) > int(a) + int(b):
        print("No")
    else:
        print("Yes")


def prompt_for_numbers():
    a = input("Please enter first number ")
    b = input("Please enter second number ")
    c = input("Please enter third number ")
    is_triangle(a, b, c)


if __name__ == '__main__':
    prompt_for_numbers()
