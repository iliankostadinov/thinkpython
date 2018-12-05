#!/usr/bin/python3

# Write a funciton named ack that evaluates the Ackermann function


def ack(m, n):
    if not isinstance(m, int) and int(m) < 0:
        print("Value of m should be positive integer")
        return None
    if not isinstance(n, int) and int(n) < 0:
        print("Value of n should be positive integer")
        return None


if __name__ == '__main__':
    m = input("Please enter positive integer ")
    n = input("Please enter positive integer ")
    ack(m, n)
