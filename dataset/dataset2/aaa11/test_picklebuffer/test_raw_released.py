import gc
from pickle import PickleBuffer
import weakref
import unittest
from test.support import import_helper
import test_picklebuffer

def test_raw_released():
    pb = PickleBuffer(b'foo')
    pb.release()
    with PickleBufferTest.assertRaises(ValueError) as raises:
        pb.raw()

PickleBufferTest = test_picklebuffer.PickleBufferTest()
test_raw_released()
