import gc
from pickle import PickleBuffer
import weakref
import unittest
from test.support import import_helper
import test_picklebuffer
class B(bytes):
    pass
def test_cycle():
    b = B(b'foo')
    pb = PickleBuffer(b)
    b.cycle = pb
    wpb = weakref.ref(pb)
    del b, pb
    gc.collect()
    PickleBufferTest.assertIsNone(wpb())

PickleBufferTest = test_picklebuffer.PickleBufferTest()
test_cycle()
