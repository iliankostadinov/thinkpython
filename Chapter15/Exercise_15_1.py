#!/usr/bin/env python3


class Point:
    """Represent a poing in 2D space

    attributes: x, y
    """


class Circle:
    """Present a circle in 2D space with
    point object for center and number for radius

    attributes: center, radius
    """


class Rectangle:
    """Present a rectangle in 2D space with
    point object for corner and numbers for widht and height

    attributes: corner, height, width
    """


def find_center(rect):
    """Takes a rectangle and return
    point which is its center

    rect: Rectangle object
    """

    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def point_in_circle(cir, p):
    """Takes a Circle and a Point and returns True if the
    Point lies in or on the boundary of the circle

    cir: Circle object
    p: Point object
    """

    if abs(cir.center.x-p.x) > cir.radius:
        return False
    if abs(cir.center.y-p.y) > cir.radius:
        return False

    return True


def rect_in_circle(cir, rect):
    """Takes a Circle and a Rectangle and returns True if
       the Rectangle lies entirely in or on the boundary of the circle

       cir: Circle object
       rect: Rectangle object
    """

    corner1 = corner2 = corner3 = corner4 = Point()
    corner1 = rect.corner
    corner2.x = corner1.x+rect.width
    corner2.y = corner1.y
    corner3.x = corner1.x+rect.width
    corner3.y = corner1.y+rect.height
    corner4.x = corner1.x
    corner4.y = corner1.y+rect.height

    if not point_in_circle(cir, corner1):
        return False
    if not point_in_circle(cir, corner2):
        return False
    if not point_in_circle(cir, corner3):
        return False
    if not point_in_circle(cir, corner4):
        return False

    return True


def rect_circle_overlap(cir, rect):
    """Takes a Circle and a Rectangle and returns True if
       any of the corners of the Rectangle fall inside the circle

       cir: Circle object
       rect: Rectangle object
    """

    corner1 = corner2 = corner3 = corner4 = Point()
    corner1 = rect.corner
    corner2.x = corner1.x+rect.width
    corner2.y = corner1.y
    corner3.x = corner1.x+rect.width
    corner3.y = corner1.y+rect.height
    corner4.x = corner1.x
    corner4.y = corner1.y+rect.height

    if point_in_circle(cir, corner1):
        return True
    if point_in_circle(cir, corner2):
        return True
    if point_in_circle(cir, corner3):
        return True
    if point_in_circle(cir, corner4):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(circle, box.corner))
    print(rect_in_circle(circle, box))
    print(rect_circle_overlap(circle, box))


if __name__ == '__main__':
    main()
