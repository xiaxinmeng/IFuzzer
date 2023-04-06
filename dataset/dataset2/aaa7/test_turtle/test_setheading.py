import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_setheading():
    TestTNavigator.nav.setheading(102.32)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), 102.32)
    TestTNavigator.nav.setheading(-123.23)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), -123.23 % 360)
    TestTNavigator.nav.setheading(-1000.34)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), -1000.34 % 360)
    TestTNavigator.nav.setheading(300000)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), 300000 % 360)

TestTNavigator = test_turtle.TestTNavigator()
test_setheading()
