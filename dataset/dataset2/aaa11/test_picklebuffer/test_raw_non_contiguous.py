import gc
from pickle import PickleBuffer
import weakref
import unittest
from test.support import import_helper
import test_picklebuffer

def test_raw_non_contiguous():
    ndarray = import_helper.import_module('_testbuffer').ndarray
    arr = ndarray(list(range(6)), shape=(6,), format='<i')[::2]
    PickleBufferTest.check_raw_non_contiguous(arr)
    arr = ndarray(list(range(12)), shape=(4, 3), format='<i')[::2]
    PickleBufferTest.check_raw_non_contiguous(arr)

PickleBufferTest = test_picklebuffer.PickleBufferTest()
test_raw_non_contiguous()
