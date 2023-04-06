import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_vector_negative():
    vec = Vec2D(10, -10)
    expected = (-10, 10)
    TestVec2D.assertVectorsAlmostEqual(-vec, expected)

TestVec2D = test_turtle.TestVec2D()
test_vector_negative()
