
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):       # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):             # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)   

    def __eq__(self, other):        # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):      # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):      # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.a = 2.2
        self.b = 5.2

    def repeat(self, f):
        j = -5
        for i in range(-10, 10):
            j += 1
            if i == 0 or j == 0: continue
            f(self.a * i, self.b * j, self.a / i, self.b / j)
            
    def test_str(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(str(Point(a, b)), "({}, {})".format(a, b)))

    def test_repr(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(repr(Point(a, b)), "Point({}, {})".format(a, b)))

    def test_eq(self):
        self.repeat(lambda a, b, c, d : self.assertTrue(Point(a, b) == Point(a, b)) or \
                                        self.assertFalse(Point(a, b + c) == Point(a - d, b)) )

    def test_ne(self):
        self.repeat(lambda a, b, c, d : self.assertTrue(Point(a, b + c) != Point(a - d, b)) or \
                                        self.assertFalse(Point(a, b) != Point(a, b)))
            
    def test_add(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Point(a, b) + Point(c, d), Point(a + c, b + d)))

    def test_sub(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Point(a, b) - Point(c, d), Point(a - c, b - d)))

    def test_mul(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Point(a, b) * Point(c, d), a * c + b * d))

    def test_cross(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Point.cross(Point(a, b), Point(c, d)), a * d - b * c))

    def test_length(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Point.length(Point(a, b)), (a ** 2 + b ** 2) ** (1/2)))

    def test_hash(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(hash(Point(a, b)), hash((a, b))))
        
    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
