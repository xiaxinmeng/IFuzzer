import gc
from pickle import PickleBuffer
import weakref
import unittest
from test.support import import_helper
import test_picklebuffer

def test_raw():
    for obj in (b'foo', bytearray(b'foo')):
        with PickleBufferTest.subTest(obj=obj):
            PickleBufferTest.check_raw(obj, obj)

PickleBufferTest = test_picklebuffer.PickleBufferTest()
test_raw()
