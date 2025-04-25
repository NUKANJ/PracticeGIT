from unittest import TestCase
import src.shape_area as area


class TestShapeArea(TestCase):
    def test_triangle(self):
        self.assertEqual(area.ShapeArea.triangle(5, 10), 25)


class TestShapeArea(TestCase):
    def test_rectangle(self):
        self.assertEqual(area.ShapeArea.rectangle(6, 7), 42)


class TestShapeArea(TestCase):
    def test_square(self):
        self.assertEqual(area.ShapeArea.square(6),36)
