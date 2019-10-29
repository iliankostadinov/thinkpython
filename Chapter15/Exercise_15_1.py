#!/usr/bin/env python3

"""Write a definition for a class named Circle with attributes center and
radius where center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at
( 150, 100 ) and radius 75. Write a function named point_in_circle that takes a
Circle and a Point and returns True if the Point lies in or on the boundary of
the circle. Write a function named rect_in_circle that takes a Circle and a
Rectangle and returns True if the Rectangle lies entirely in or on the boundary
of the circle. Write a function named rect_circle_overlap that takes a Circle
and a Rectangle and returns True if any of the corners of the Rectangle fall
inside the circle. Or as a more challenging version, return True if any part
of the Rectangle falls inside the circle.
"""


class Point:
    """Represent a point in 2D space.
    attributes: x, y
    """


class Circle:
    """Represent a circle in 2-D space.
    atributes: center which is Point object and radius
    """


class Rectangle:
    """Present a Rectangle in 2-D space.
    atributes: points in opposite corners
    """


def point_in_circle(cir, poin):
    """Return True if point lies in boundary of the circle

    cir: Circle object
    poin: Point ojbect
    """
    if abs(cir.center.x - poin.x) > cir.radius:
        return False
    elif abs(cir.center.y - poin.y) > cir.radius:
        return False
    else:
        return True


def rect_in_circle(cir, rect):
    """Return True if Rectangle lies in boundary of the circle

    cir: Circle object
    rect: Rectangle object
    """
    corner_1 = Point()
    corner_1.x = rect.p1.x
    corner_1.y = rect.p1.y
    corner_2 = Point()
    corner_2.x = rect.p1.x
    corner_2.y = rect.p2.y
    corner_3 = Point()
    corner_3.x = rect.p2.x
    corner_3.y = rect.p1.y
    corner_4 = Point()
    corner_4.x = rect.p2.y
    corner_4.y = rect.p1.x

    if point_in_circle(cir, corner_1):
        pass
    else:
        return False
    if point_in_circle(cir, corner_2):
        pass
    else:
        return False
    if point_in_circle(cir, corner_3):
        pass
    else:
        return False
    if point_in_circle(cir, corner_4):
        pass
    else:
        return False

    return True


def rect_circle_overlap(cir, rect):
    """Return True if any part of Rectangle overlap circle

    cir: Circle object
    rect: Rectangle object
    """

    corner_1 = Point()
    corner_1.x = rect.p1.x
    corner_1.y = rect.p1.y
    corner_2 = Point()
    corner_2.x = rect.p1.x
    corner_2.y = rect.p2.y
    corner_3 = Point()
    corner_3.x = rect.p2.x
    corner_3.y = rect.p1.y
    corner_4 = Point()
    corner_4.x = rect.p2.y
    corner_4.y = rect.p1.x

    if point_in_circle(cir, corner_1):
        return True
    if point_in_circle(cir, corner_2):
        return True
    if point_in_circle(cir, corner_3):
        return True
    if point_in_circle(cir, corner_4):
        return True

    return False


if __name__ == "__main__":
    center = Point()
    center.x = 15
    center.y = 10

    p = Point()
    p.x = 20
    p.y = 30

    c = Circle()
    c.center = center
    c.radius = 75

    p1 = Point()
    p2 = Point()
    p1.x = 20
    p1.y = 30
    p2.x = 10
    p2.y = 5

    rect = Rectangle()
    rect.p1 = p1
    rect.p2 = p2

    if point_in_circle(c, p):
        print("Point is in circle!")
    else:
        print("Point is not in circle")

    if rect_in_circle(c, rect):
        print("Rectangle is in circle!")
    else:
        print("Rectangle is not in circle")
