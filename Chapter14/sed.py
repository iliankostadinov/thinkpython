#!/usr/bin/env python3

"""
    Write a function called sed that takes as arguments a pattern string, a replacement
    string, and two filenames; it should read the first file and write the contents into the second file
    (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
    with the replacement string.
    If an error occurs while opening, reading, writing or closing files, your program should catch the
    exception, print an error message, and exit.
"""


def sed(patern, replacement, s_file, d_file):
    try:
        source_f = open(s_file, mode='r')
        dest_f = open(d_file, mode='a')
        content = source_f.read()
        dest_f.write(content.replace(patern, replacement))
    except:
        print("Something went wrong")


if __name__ == "__main__":
    sed("gosho", "ilian", "file_s", "file_d")
