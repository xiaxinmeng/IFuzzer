import itertools
import operator
import sys
import unittest
import weakref
from pickle import loads, dumps
from test import support
import test_slice

def test_repr():
    SliceTest.assertEqual(repr(slice(1, 2, 3)), 'slice(1, 2, 3)')

SliceTest = test_slice.SliceTest()
test_repr()
