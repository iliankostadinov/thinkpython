#!/usr/bin/env python3

"""Write a function called draw_rect that takes a Turtle object and a
   Rectangle and uses the Turtle to draw the Rectangle
"""

import turtle


class Rectangle:
    """Represent rectangle in 2D space defined by,
    corner, height and weight.

    attributes: corner, height, weight
    """


class Point:
    """Represent point in 2D space.
    attributes: x, y
    """


def draw_rect(tur, rect):
    tur.pu()
    tur.fd(rect.corner.x)
    tur.lt(90)
    tur.fd(rect.corner.y)
    tur.rt(90)
    tur.pd()
    tur.fd(rect.weight)
    tur.lt(90)
    tur.fd(rect.height)
    tur.lt(90)
    tur.fd(rect.weight)
    tur.lt(90)
    tur.fd(rect.height)
    turtle.mainloop()


if __name__ == "__main__":
    bob = turtle.Turtle()
    p = Point()
    p.x = 30
    p.y = 50
    re = Rectangle()
    re.corner = p
    re.height = 100
    re.weight = 200
    draw_rect(bob, re)
