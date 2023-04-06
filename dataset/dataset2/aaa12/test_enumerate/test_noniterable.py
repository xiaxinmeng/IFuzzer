import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_noniterable():
    EnumerateTestCase.assertRaises(TypeError, EnumerateTestCase.enum, test_enumerate.X(EnumerateTestCase.seq))

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_noniterable()
