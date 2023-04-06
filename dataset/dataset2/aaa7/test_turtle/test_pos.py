import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_pos():
    TestTNavigator.assertEqual(TestTNavigator.nav.pos(), TestTNavigator.nav._position)
    TestTNavigator.nav.goto(100, -100)
    TestTNavigator.assertEqual(TestTNavigator.nav.pos(), TestTNavigator.nav._position)

TestTNavigator = test_turtle.TestTNavigator()
test_pos()
