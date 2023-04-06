import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_illformediterable():
    EnumerateTestCase.assertRaises(TypeError, EnumerateTestCase.enum, test_enumerate.N(EnumerateTestCase.seq))

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_illformediterable()
