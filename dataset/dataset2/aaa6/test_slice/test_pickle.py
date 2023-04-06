import itertools
import operator
import sys
import unittest
import weakref
from pickle import loads, dumps
from test import support
import test_slice

def test_pickle():
    s = slice(10, 20, 3)
    for protocol in (0, 1, 2):
        t = loads(dumps(s, protocol))
        SliceTest.assertEqual(s, t)
        SliceTest.assertEqual(s.indices(15), t.indices(15))
        SliceTest.assertNotEqual(id(s), id(t))

SliceTest = test_slice.SliceTest()
test_pickle()
