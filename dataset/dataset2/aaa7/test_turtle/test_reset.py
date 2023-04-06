import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_reset():
    TestTNavigator.nav.goto(100, -100)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.xcor(), 100)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.ycor(), -100)
    TestTNavigator.nav.reset()
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.xcor(), 0)
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.ycor(), 0)

TestTNavigator = test_turtle.TestTNavigator()
test_reset()
