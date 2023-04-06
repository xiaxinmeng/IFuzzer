import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_setx_and_sety():
    TestTNavigator.nav.setx(-1023.2334)
    TestTNavigator.nav.sety(193323.234)
    TestTNavigator.assertVectorsAlmostEqual(TestTNavigator.nav.pos(), (-1023.2334, 193323.234))

TestTNavigator = test_turtle.TestTNavigator()
test_setx_and_sety()
