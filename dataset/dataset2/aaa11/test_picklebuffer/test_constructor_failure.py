import gc
from pickle import PickleBuffer
import weakref
import unittest
from test.support import import_helper
import test_picklebuffer

def test_constructor_failure():
    with PickleBufferTest.assertRaises(TypeError):
        PickleBuffer()
    with PickleBufferTest.assertRaises(TypeError):
        PickleBuffer('foo')
    m = memoryview(b'foo')
    m.release()
    with PickleBufferTest.assertRaises(ValueError):
        PickleBuffer(m)

PickleBufferTest = test_picklebuffer.PickleBufferTest()
test_constructor_failure()
