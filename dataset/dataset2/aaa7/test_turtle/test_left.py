import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_left():
    TestTNavigator.assertEqual(TestTNavigator.nav._orient, (1.0, 0))
    TestTNavigator.nav.left(90)
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav._orient, (0.0, 1.0))

TestTNavigator = test_turtle.TestTNavigator()
test_left()
