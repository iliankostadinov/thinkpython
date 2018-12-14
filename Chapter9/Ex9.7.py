#!/usr/bin/env python3

"""
 Find a word with three consecutive double letters. Word which almost qualify
 is committee, but it has i between m and t
"""


def is_three_cosecutive(syllables):
    if syllables[0] == syllables[1] and syllables[2] == syllables[3] and syllables[4] == syllables[5]:
        return True
    else:
        return False


def check_word(line):
    while len(line) > 5:
        temp = ""
        for i in range(0, 6):
            temp = temp + line[i]
        if is_three_cosecutive(temp):
            return True
        line = line.lstrip(line[0])
    return False


if __name__ == "__main__":
    fin = open("words.txt")
    for line in fin:
        stripped = line.strip()
        if len(stripped) < 6:
            continue
        if check_word(stripped):
            print(stripped)
