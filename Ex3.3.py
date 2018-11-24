#!/usr/bin/python3


# Printing grid four by four using only things learned till this chapter
def print_grid(val):
    print_hor(val)
    print_hor(val)
    print_hor(val)
    print_hor(val)


def print_hor(val):
    print(val*'+ - - - - ', end='')
    print('+')
    print(val*'|         ', end='')
    print("|")
    print(val*'|         ', end='')
    print("|")
    print(val*'|         ', end='')
    print("|")
    print(val*'+ - - - - ', end='')
    print('+', end='\r')


if __name__ == '__main__':
    print_grid(4)
    print()
