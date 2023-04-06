import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_distance():
    TestVec2D.nav.forward(100)
    expected = 100
    TestVec2D.assertAlmostEqual(TestVec2D.nav.distance(Vec2D(0, 0)), expected)

TestVec2D = test_turtle.TestVec2D()
test_distance()
