import unittest
import math

from task_01_duck_typing import Circle, Rectangle  # adapte le nom si ton fichier s'appelle autrement


class TestCircle(unittest.TestCase):

    def test_area(self):
        c = Circle(3)
        self.assertAlmostEqual(c.area(), math.pi * 9)

    def test_perimeter(self):
        c = Circle(3)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 3)


class TestRectangle(unittest.TestCase):

    def test_area(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_perimeter(self):
        r = Rectangle(4, 5)
        self.assertEqual(r.perimeter(), 18)


if __name__ == "__main__":
    unittest.main()
