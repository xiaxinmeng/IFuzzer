import unittest
import operator
import sys
import pickle
import gc
from test import support
import test_enumerate

@support.cpython_only
def test_enumerate_result_gc():
    it = EnumerateTestCase.enum([[]])
    gc.collect()
    EnumerateTestCase.assertTrue(gc.is_tracked(next(it)))

EnumerateTestCase = test_enumerate.EnumerateTestCase()
test_enumerate_result_gc()
