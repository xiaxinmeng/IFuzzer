import itertools
import operator
import sys
import unittest
import weakref
from pickle import loads, dumps
from test import support
import test_slice

def test_cycle():

    class myobj:
        pass
    o = myobj()
    o.s = slice(o)
    w = weakref.ref(o)
    o = None
    support.gc_collect()
    SliceTest.assertIsNone(w())

SliceTest = test_slice.SliceTest()
test_cycle()
