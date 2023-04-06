import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_home():
    TestTNavigator.nav.left(30)
    TestTNavigator.nav.forward(-100000)
    TestTNavigator.nav.home()
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav.pos(), (0, 0))
    TestTNavigator.assertAlmostEqual(TestTNavigator.nav.heading(), 0)

TestTNavigator = test_turtle.TestTNavigator()
test_home()
