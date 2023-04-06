import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_iteratorseqn():
    EnumerateTestCase.assertEqual(list(EnumerateTestCase.enum(test_enumerate.I(EnumerateTestCase.seq))), EnumerateTestCase.res)
    e = EnumerateTestCase.enum(test_enumerate.I(''))
    EnumerateTestCase.assertRaises(StopIteration, next, e)

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_iteratorseqn()
