#!/usr/bin/env python3

"""
 Write a prgogram that reads words.txt and prints only the words with more
 then 20 characters (not counting whitespace)
"""


if __name__ == "__main__":
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
