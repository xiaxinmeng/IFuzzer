import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_distance_method():
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.distance(30, 40), 50)
    vec = Vec2D(0.22, 0.001)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.distance(vec), 0.22000227271553355)
    another_turtle = turtle.TNavigator()
    another_turtle.left(90)
    another_turtle.forward(10000)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.distance(another_turtle), 10000)

TestTNavigator = test_turtle.TestTNavigator()
test_distance_method()
