import itertools
import operator
import sys
import unittest
import weakref
from pickle import loads, dumps
from test import support
import test_slice

def test_members():
    s = slice(1)
    SliceTest.assertEqual(s.start, None)
    SliceTest.assertEqual(s.stop, 1)
    SliceTest.assertEqual(s.step, None)
    s = slice(1, 2)
    SliceTest.assertEqual(s.start, 1)
    SliceTest.assertEqual(s.stop, 2)
    SliceTest.assertEqual(s.step, None)
    s = slice(1, 2, 3)
    SliceTest.assertEqual(s.start, 1)
    SliceTest.assertEqual(s.stop, 2)
    SliceTest.assertEqual(s.step, 3)

    class AnyClass:
        pass
    obj = AnyClass()
    s = slice(obj)
    SliceTest.assertTrue(s.stop is obj)

SliceTest = test_slice.SliceTest()
test_members()
