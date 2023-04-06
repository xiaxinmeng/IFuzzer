import gc
from pickle import PickleBuffer
import weakref
import unittest
from test.support import import_helper
import test_picklebuffer

def test_basics():
    pb = PickleBuffer(b'foo')
    PickleBufferTest.assertEqual(b'foo', bytes(pb))
    with memoryview(pb) as m:
        PickleBufferTest.assertTrue(m.readonly)
    pb = PickleBuffer(bytearray(b'foo'))
    PickleBufferTest.assertEqual(b'foo', bytes(pb))
    with memoryview(pb) as m:
        PickleBufferTest.assertFalse(m.readonly)
        m[0] = 48
    PickleBufferTest.assertEqual(b'0oo', bytes(pb))

PickleBufferTest = test_picklebuffer.PickleBufferTest()
test_basics()
