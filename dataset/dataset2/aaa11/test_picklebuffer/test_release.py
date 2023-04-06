import gc
from pickle import PickleBuffer
import weakref
import unittest
from test.support import import_helper
import test_picklebuffer

def test_release():
    pb = PickleBuffer(b'foo')
    pb.release()
    with PickleBufferTest.assertRaises(ValueError) as raises:
        memoryview(pb)
    PickleBufferTest.assertIn('operation forbidden on released PickleBuffer object', str(raises.exception))
    pb.release()

PickleBufferTest = test_picklebuffer.PickleBufferTest()
test_release()
