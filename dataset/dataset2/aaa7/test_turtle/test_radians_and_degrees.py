import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_radians_and_degrees():
    TestTNavigator.nav.left(90)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), 90)
    TestTNavigator.nav.radians()
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), 1.57079633)
    TestTNavigator.nav.degrees()
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), 90)

TestTNavigator = test_turtle.TestTNavigator()
test_radians_and_degrees()
