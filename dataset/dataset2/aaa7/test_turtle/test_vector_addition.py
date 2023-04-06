import pickle
import unittest
from test import support
from test.support import import_helper
from test.support import os_helper
import test_turtle

def test_vector_addition():
    test_cases = [(((0, 0), (1, 1)), (1.0, 1.0)), (((-1, 0), (2, 2)), (1, 2)), (((1.5, 0), (1, 1)), (2.5, 1))]
    TestVec2D._assert_arithmetic_cases(test_cases, lambda x, y: x + y)

TestVec2D = test_turtle.TestVec2D()
test_vector_addition()
