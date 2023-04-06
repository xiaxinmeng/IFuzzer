import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

def test_getitemseqn():
    EnumerateTestCase.assertEqual(list(EnumerateTestCase.enum(test_enumerate.G(EnumerateTestCase.seq))), EnumerateTestCase.res)
    e = EnumerateTestCase.enum(test_enumerate.G(''))
    EnumerateTestCase.assertRaises(StopIteration, next, e)

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_getitemseqn()
