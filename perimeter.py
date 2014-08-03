#!/usr/bin/env python
import csv
import glob
import os
import sys


def calculate_length(file_name):
    """
    read a list of points from a CSV file and print out the length of the perimeter of the shape that is formed by
    joining the points in their listed order
    """
    fp = open(file_name)
    reader = csv.reader(fp)

    points = []
    for row in reader:
        x = try_parse(row[0])
        y = try_parse(row[1])
        if x is not None and y is not None:
            points.append((x, y))

    return perimeter(points)


def try_parse(string, fail=None):
    try:
        return float(string)
    except Exception:
        return fail


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

    if len(points) == 1:  # single point, no distance
        return distances

    for i in range(len(points)):
        point = points[i]

        if len(points) > i + 1:
            next_point = points[i + 1]
        else:
            if len(points) > 2:
                next_point = points[0]
            else:
                next_point = None  # 2 point it's a line, only one distance

        if next_point is not None:
            x0 = point[0]
            y0 = point[1]
            x1 = next_point[0]
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
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isdir(path):
            csvfiles = glob.glob("{}/*.csv".format(sys.argv[1]))
            for csvfile in csvfiles:
                print "{} \t {}".format(csvfile, calculate_length(csvfile))
        else:
            if os.path.isfile(path):
                print calculate_length(path)
            else:
                print "File not found"
    else:
        print "Please enter file or folder path"