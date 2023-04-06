import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_forward():
    TestTNavigator.nav.forward(150)
    expected = Vec2D(150, 0)
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav.position(), expected)
    TestTNavigator.nav.reset()
    TestTNavigator.nav.left(90)
    TestTNavigator.nav.forward(150)
    expected = Vec2D(0, 150)
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav.position(), expected)
    TestTNavigator.assertRaises(TypeError, TestTNavigator.nav.forward, 'skldjfldsk')

TestTNavigator = test_turtle.TestTNavigator()
test_forward()
