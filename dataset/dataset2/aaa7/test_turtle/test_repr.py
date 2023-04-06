import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_repr():
    vec = Vec2D(0.567, 1.234)
    TestVec2D.assertEqual(repr(vec), '(0.57,1.23)')

TestVec2D = test_turtle.TestVec2D()
test_repr()
