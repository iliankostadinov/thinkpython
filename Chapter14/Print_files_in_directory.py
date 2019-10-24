#!/usr/bin/env python3

import os


def walk(dirname):
    for names in os.listdir(dirname):
        path = os.path.join(dirname, names)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    for root, dirs, files in os.walk(dirname):
        for filenames in files:
            print(os.path.join(root, filenames))


if __name__ == "__main__":

    directory = input("Please enter directory name")
    if os.path.isdir(directory):
        walk(directory)
    else:
        print("Please enter directory name")

    walk(directory)
#    walk2(directory)
