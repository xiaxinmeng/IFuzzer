import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_positions():
    TestTNavigator.nav.forward(100)
    TestTNavigator.nav.left(90)
    TestTNavigator.nav.forward(-200)
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav.pos(), (100.0, -200.0))

TestTNavigator = test_turtle.TestTNavigator()
test_positions()
