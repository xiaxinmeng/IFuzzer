import unittest
from test import support
import io
import _pyio as pyio
import pickle
import sys
import __main__
import array
import array
import test_memoryio

@support.cpython_only
def test_cow_mutable():
    ba = bytearray(1024)
    old_rc = sys.getrefcount(ba)
    memio = CBytesIOTest.ioclass(ba)
    CBytesIOTest.assertEqual(sys.getrefcount(ba), old_rc)

CBytesIOTest = test_memoryio.CBytesIOTest()
test_cow_mutable()
