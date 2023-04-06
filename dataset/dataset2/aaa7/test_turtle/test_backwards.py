import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_backwards():
    TestTNavigator.nav.back(200)
    expected = Vec2D(-200, 0)
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav.position(), expected)
    TestTNavigator.nav.reset()
    TestTNavigator.nav.right(90)
    TestTNavigator.nav.back(200)
    expected = Vec2D(0, 200)
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav.position(), expected)

TestTNavigator = test_turtle.TestTNavigator()
test_backwards()
