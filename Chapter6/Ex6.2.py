#!/usr/bin/python3

# Write a funciton named ack that evaluates the Ackermann function

def ack(m, n):
    if not isinstance(m, int) and int(m) < 0:
        print("Value of m should be positive integer")
        return None
    if not isinstance(n, int) and int(n) < 0:
        print("Value of n should be positive integer")
        return None
    if int(m) == 0:
        return int(n) + 1
    if int(m) > 0 and int(n) == 0:
        return ack(int(m)-1, 1)
    else:
        return ack(int(m)-1, ack(m, int(n)-1))


if __name__ == '__main__':
    m = input("Please enter positive integer ")
    n = input("Please enter positive integer ")
    value = ack(m, n)
    print(value)
