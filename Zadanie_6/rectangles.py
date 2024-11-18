from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):        # obsługa rect1 == rect2
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2) or \
               (self.pt1 == other.pt2 and self.pt2 == other.pt1)


    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):                 # pole powierzchni
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
                
    def setUp(self):
        self.a = 2.2
        self.b = 5.2
        self.c = 7.2
        self.d = 11.2

    def repeat(self, f):
        j = -5
        for i in range(-10, 10):
            j += 1
            if i == 0 or j == 0: continue
            f(self.a * i, self.b * j, self.a / i, self.b / j)

    def test_str(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(str(Rectangle(a, b, c, d)), "[({}, {}), ({}, {})]".format(a, b, c, d)))

    def test_repr(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(repr(Rectangle(a, b, c, d)), "Rectangle({}, {}, {}, {})".format(a, b, c, d)))

    def test_eq(self):
        self.repeat(lambda a, b, c, d : self.assertTrue(Rectangle(a, b, c, d) == Rectangle(a, b, c, d)) or \
                                        self.assertFalse(Rectangle(a, b, c, d) == Rectangle(a, c, b, d)))

    def test_ne(self):
        self.repeat(lambda a, b, c, d : self.assertFalse(Rectangle(a, b, c, d) != Rectangle(a, b, c, d)) or \
                                        self.assertTrue(Rectangle(a, b, c, d) != Rectangle(a, c, b, d)))

    def test_center(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Rectangle(a, b, c, d).center(), Point((a + c) / 2, (b + d) / 2)))
        

    def test_area(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Rectangle(a, b, c, d).area(), abs(a - c) * abs(b - d)))

    def test_move(self):
        self.repeat(lambda a, b, c, d : self.assertEqual(Rectangle(a, b, c, d).move(a, b), Rectangle(a + a, b + b, c + a, d + b)))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
