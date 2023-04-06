import copy
import gc
import pickle
import sys
import unittest
import weakref
import inspect
from test import support
import _testcapi
from test import support, test_generators
import test_generators

def test_frame_resurrect():

    def gen():
        nonlocal frame
        try:
            yield
        finally:
            frame = sys._getframe()
    g = gen()
    wr = weakref.ref(g)
    next(g)
    del g
    support.gc_collect()
    FinalizationTest.assertIs(wr(), None)
    FinalizationTest.assertTrue(frame)
    del frame
    support.gc_collect()

FinalizationTest = test_generators.FinalizationTest()
test_frame_resurrect()
