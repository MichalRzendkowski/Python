from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2: raise ValueError
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):        # obsługa rect1 == rect2
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):                 # pole powierzchni
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other): # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1<x2 and y1<y2: return Rectangle(x1, y1, x2, y2)
        raise ValueError

    def cover(self, other):         # prostąkąt nakrywający oba
        return Rectangle(min(self.pt1.x, other.pt1.x),\
                         min(self.pt1.y, other.pt1.y),\
                         max(self.pt2.x, other.pt2.x),\
                         max(self.pt2.y, other.pt2.y))

    def make4(self):                # zwraca krotkę czterech mniejszych
        rec1 = Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y)
        rec2 = Rectangle(self.pt1.x, self.center().y, self.center().x, self.pt2.y)
        rec3 = Rectangle(self.center().x, self.center().y, self.pt2.x, self.pt2.y)
        rec4 = Rectangle(self.center().x, self.pt1.y, self.pt2.x, self.center().y)
        return (rec1, rec2, rec3, rec4)


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    
    def test_init(self):
        with self.assertRaises(ValueError): Rectangle(3, 4, 1, 2)
        with self.assertRaises(ValueError): Rectangle(1, 2, -1, -2)
        with self.assertRaises(ValueError): Rectangle(-1, -2, -3, -4)
    
    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")
        self.assertEqual(str(Rectangle(-4, -3, -2, -1)), "[(-4, -3), (-2, -1)]")
        self.assertEqual(str(Rectangle(0, 0, 5, 5)), "[(0, 0), (5, 5)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(Rectangle(-4, -3, -2, -1)), "Rectangle(-4, -3, -2, -1)")
        self.assertEqual(repr(Rectangle(0, 0, 5, 5)), "Rectangle(0, 0, 5, 5)")

    def test_eq(self):
        self.assertTrue(Rectangle(1, 1, 4, 5) == Rectangle(1, 1, 4, 5))
        self.assertFalse(Rectangle(1, 1, 4, 5) == Rectangle(1, 1, 4, 6))
        self.assertFalse(Rectangle(1, 1, 4, 5) == Rectangle(2, 2, 5, 6))

    def test_ne(self):
        self.assertTrue(Rectangle(1, 1, 4, 5) != Rectangle(2, 2, 5, 6))
        self.assertTrue(Rectangle(1, 1, 4, 5) != Rectangle(1, 1, 4, 6))
        self.assertFalse(Rectangle(1, 1, 4, 5) != Rectangle(1, 1, 4, 5))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).center(), Point(2, 2))
        self.assertEqual(Rectangle(1, 2, 5, 6).center(), Point(3, 4))
        self.assertEqual(Rectangle(-3, -2, 1, 4).center(), Point(-1, 1))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 1, 1).area(), 1)
        self.assertEqual(Rectangle(0, 0, 3, 4).area(), 12)
        self.assertEqual(Rectangle(-3, -2, 1, 4).area(), 24)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 1, 1).move(1, 1), Rectangle(1, 1, 2, 2))
        self.assertEqual(Rectangle(1, 2, 3, 4).move(-1, -1), Rectangle(0, 1, 2, 3))
        self.assertEqual(Rectangle(-3, -2, 1, 4).move(3, 2), Rectangle(0, 0, 4, 6))

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 6, 6).intersection(Rectangle(2, 2, 8, 8)), Rectangle(2, 2, 6, 6))
        self.assertEqual(Rectangle(0, 0, 6, 6).intersection(Rectangle(2, 2, 4, 4)), Rectangle(2, 2, 4, 4))
        self.assertEqual(Rectangle(0, 0, 4, 4).intersection(Rectangle(0, 0, 4, 4)), Rectangle(0, 0, 4, 4))
        with self.assertRaises(ValueError): Rectangle(0, 0, 2, 2).intersection(Rectangle(3, 3, 5, 5))
        with self.assertRaises(ValueError): Rectangle(0, 0, 3, 3).intersection(Rectangle(3, 0, 6, 3))

    def test_cover(self):
        self.assertEqual(Rectangle(0, 0, 1, 1).cover(Rectangle(0, 0, 1, 1)), Rectangle(0, 0, 1, 1))
        self.assertEqual(Rectangle(1, 2, 3, 4).cover(Rectangle(2, 1, 4, 3)), Rectangle(1, 1, 4, 4))
        self.assertEqual(Rectangle(-3, -2, 1, 4).cover(Rectangle(0, 0, 2, 6)), Rectangle(-3, -2, 2, 6))

    def test_make4(self):
        rec1, rec2, rec3, rec4 = Rectangle(0, 0, 4, 4).make4()
        self.assertEqual(rec1, Rectangle(0, 0, 2, 2))
        self.assertEqual(rec2, Rectangle(0, 2, 2, 4))
        self.assertEqual(rec3, Rectangle(2, 2, 4, 4))
        self.assertEqual(rec4, Rectangle(2, 0, 4, 2))

        rec1, rec2, rec3, rec4 = Rectangle(1, 2, 5, 6).make4()
        self.assertEqual(rec1, Rectangle(1, 2, 3, 4))
        self.assertEqual(rec2, Rectangle(1, 4, 3, 6))
        self.assertEqual(rec3, Rectangle(3, 4, 5, 6))
        self.assertEqual(rec4, Rectangle(3, 2, 5, 4))

if __name__ == '__main__':
    unittest.main()
