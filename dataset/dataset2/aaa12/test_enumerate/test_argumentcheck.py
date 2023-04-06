import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_argumentcheck():
    EnumerateTestCase.assertRaises(TypeError, EnumerateTestCase.enum)
    EnumerateTestCase.assertRaises(TypeError, EnumerateTestCase.enum, 1)
    EnumerateTestCase.assertRaises(TypeError, EnumerateTestCase.enum, 'abc', 'a')
    EnumerateTestCase.assertRaises(TypeError, EnumerateTestCase.enum, 'abc', 2, 3)

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_argumentcheck()
