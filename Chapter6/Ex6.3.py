#!/usr/bin/env python3

# Check if entered string is palindrome


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 2 and first(word) == last(word):
        return True
    if len(word) == 3 and first(word) == last(word):
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('nooxn'))
