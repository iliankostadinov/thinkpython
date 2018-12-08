#!/usr/bin/env python3

"""
 Write online version of is_palindrome
"""


if __name__ == "__main__":
    input_sring = "madam"
    if input_sring[::-1] == input_sring:
        print("String is palindrome")
    else:
        print("Sring is not palindrome")
