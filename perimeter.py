#!/usr/bin/env python
import csv
import sys


def main(file_name):
    """
    read a list of points from a CSV file and print out the length of the perimeter of the shape that is formed by
    joining the points in their listed order
    """
    fp = open(file_name)
    reader = csv.reader(fp)

    points = []
    for row in reader:
        x = row[0]
        y = row[1]
        points.append((x, y))

    length = perimeter(points)

    print length


def perimeter(points):
    """ returns the length of the perimeter of some shape defined by a list of points """
    distances = get_distances(points)

    length = 0
    for distance in distances:
        length = length + distance

    return length


def get_distances(points):
    """ convert a list of points into a list of distances """
    i = 0
    distances = []
    for i in range(len(points)):
        point = points[i]
        next_point = points[i + 1]
        x0 = point[0]
        y0 = point[1]
        x1 = next_point[1]
        y1 = next_point[1]

        point_distance = get_distance(x0, y0, x1, y1)
        distances.append(point_distance)

    return distances


def get_distance(x1, y1, x2, y2):
    """ use pythagorean theorem to find distance between 2 points """
    a = x2 - x1
    b = y2 - y1
    c_2 = a * a + b * b

    return c_2 ** .5


if __name__ == "__main__":
    path = sys.argv[0]
    main(path)