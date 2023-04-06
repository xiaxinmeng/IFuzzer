import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_exception_propagation():
    EnumerateTestCase.assertRaises(ZeroDivisionError, list, EnumerateTestCase.enum(test_enumerate.E(EnumerateTestCase.seq)))

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_exception_propagation()
