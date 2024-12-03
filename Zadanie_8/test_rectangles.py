from rectangles import Rectangle
from points import Point
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

    def test_from_points(self):
        self.assertEqual(Rectangle.from_points((Point(1, 2), Point(5, 6))), Rectangle(1, 2, 5, 6))
        self.assertEqual(Rectangle.from_points((Point(0, 0), Point(3, 4))), Rectangle(0, 0, 3, 4))
        with self.assertRaises(ValueError): Rectangle.from_points((Point(1, 2)))

    def test_top(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).top, 6)
        self.assertEqual(Rectangle(0, 0, 4, 3).top, 3)
        self.assertEqual(Rectangle(-3, -2, 2, 1).top, 1)

    def test_left(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).left, 1)
        self.assertEqual(Rectangle(0, 0, 4, 3).left, 0)
        self.assertEqual(Rectangle(-3, -2, 2, 1).left, -3)

    def test_bottom(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).bottom, 2)
        self.assertEqual(Rectangle(0, 0, 4, 3).bottom, 0)
        self.assertEqual(Rectangle(-3, -2, 2, 1).bottom, -2)

    def test_right(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).right, 5)
        self.assertEqual(Rectangle(0, 0, 4, 3).right, 4)
        self.assertEqual(Rectangle(-3, -2, 2, 1).right, 2)

    def test_width(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).width, 4)
        self.assertEqual(Rectangle(0, 0, 4, 3).width, 4)
        self.assertEqual(Rectangle(-3, -2, 2, 1).width, 5)

    def test_height(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).height, 4)
        self.assertEqual(Rectangle(0, 0, 4, 3).height, 3)
        self.assertEqual(Rectangle(-3, -2, 2, 1).height, 3)

    def test_topleft(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).topleft, Point(1, 6))
        self.assertEqual(Rectangle(0, 0, 4, 3).topleft, Point(0, 3))
        self.assertEqual(Rectangle(-3, -2, 2, 1).topleft, Point(-3, 1))

    def test_bottomleft(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).bottomleft, Point(1, 2))
        self.assertEqual(Rectangle(0, 0, 4, 3).bottomleft, Point(0, 0))
        self.assertEqual(Rectangle(-3, -2, 2, 1).bottomleft, Point(-3, -2))

    def test_topright(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).topright, Point(5, 6))
        self.assertEqual(Rectangle(0, 0, 4, 3).topright, Point(4, 3))
        self.assertEqual(Rectangle(-3, -2, 2, 1).topright, Point(2, 1))

    def test_bottomright(self):
        self.assertEqual(Rectangle(1, 2, 5, 6).bottomright, Point(5, 2))
        self.assertEqual(Rectangle(0, 0, 4, 3).bottomright, Point(4, 0))
        self.assertEqual(Rectangle(-3, -2, 2, 1).bottomright, Point(2, -2))

if __name__ == '__main__':
    unittest.main()
