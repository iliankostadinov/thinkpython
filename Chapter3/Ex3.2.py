#!/usr/bin/python3


# f is a function object v is a value passed to it
def do_twice(f, v):
    f(v)
    f(v)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


if __name__ == '__main__':
    val = "spam"
    do_four(print_twice, val)
