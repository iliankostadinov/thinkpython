#!/usr/bin/env python3

"""
Write a definition for a class named Kangaroo with the following methods:
1. An __init__ method that initializes an attribute named pouch_contents to an
empty list.
2. A method named put_in_pouch that takes an object of any type and adds it to
pouch_contents .

3. A __str__ method that returns a string representation of the Kangaroo object
and the contents of the pouch.

Test your code by creating two Kangaroo objects, assigning them to variables
named kanga and roo , and then adding roo to the contents of kangas pouch.
"""


class Kangaroo(object):
    """Define Kangaroo class """

    def __init__(self, name, pouch_contents=None):
        self.name = name
        if pouch_contents is None:
            pouch_contents = []
        self.pouch_contents = pouch_contents

    def __str__(self):
        t = ["Object " + self.name]
        for obj in self.pouch_contents:
            s = ' ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds new ittem to the pouch_contents
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
