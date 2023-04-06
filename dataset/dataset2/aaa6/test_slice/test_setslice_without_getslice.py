import itertools
import operator
import sys
import unittest
import weakref
from pickle import loads, dumps
from test import support
import test_slice

def test_setslice_without_getslice():
    tmp = []

    class X(object):

        def __setitem__(SliceTest, i, k):
            tmp.append((i, k))
    x = X()
    x[1:2] = 42
    SliceTest.assertEqual(tmp, [(slice(1, 2), 42)])

SliceTest = test_slice.SliceTest()
test_setslice_without_getslice()
