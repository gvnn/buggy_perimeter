import math
import unittest
import sys

import perimeter


class TestPerimeter(unittest.TestCase):
    def test_get_distance(self):
        distance = perimeter.get_distance(0, 0, 0, 0)
        self.assertEqual(distance, 0)
        distance = perimeter.get_distance(0, 0, 1, 1)
        self.assertEqual(distance, math.sqrt(2))
        # testing couple of Pythagorean triples
        distance = perimeter.get_distance(1, 1, 4, 5)
        self.assertEqual(distance, 5)
        distance = perimeter.get_distance(1, 1, 6, 13)
        self.assertEqual(distance, 13)
        distance = perimeter.get_distance(1, 1, 22, 21)
        self.assertEqual(distance, 29)
        # no errors
        distance = perimeter.get_distance(-sys.maxint - 1, -sys.maxint - 1, sys.maxint, sys.maxint)

    def test_get_distances(self):
        # one point, no distance
        distances = perimeter.get_distances([(10, -19)])
        self.assertEqual(len(distances), 0)
        distances = perimeter.get_distances([(1, 1), (120, 121)])
        self.assertEqual(len(distances), 1)
        self.assertEqual(distances[0], 169)
        distances = perimeter.get_distances([(-24, -2), (11, 10), (130, 130)])
        self.assertEqual(distances[0], 37)
        self.assertEqual(distances[1], 169)

    def test_perimeter(self):
        square_perimeter = perimeter.perimeter([(0, 0), (10, 0), (10, 10), (0, 10)])
        self.assertEqual(square_perimeter, 40)
        triangle_perimeter = perimeter.perimeter([[0, 0], [0, 3], [4, 0]])
        self.assertEqual(triangle_perimeter, 12)

    def test_polygon_perimeter(self):
        length = perimeter.calculate_length('./sample_data/rand1.csv')
        self.assertGreater(length, 0)
        square_perimeter = perimeter.calculate_length('./sample_data/square.csv')
        self.assertEqual(square_perimeter, 40)


if __name__ == '__main__':
    unittest.main()