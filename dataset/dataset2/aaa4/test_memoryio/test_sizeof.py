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
def test_sizeof():
    basesize = support.calcobjsize('P2n2Pn')
    check = CBytesIOTest.check_sizeof
    CBytesIOTest.assertEqual(object.__sizeof__(io.BytesIO()), basesize)
    check(io.BytesIO(), basesize)
    n = 1000
    check(io.BytesIO(b'a' * n), basesize + sys.getsizeof(b'a' * n))

CBytesIOTest = test_memoryio.CBytesIOTest()
test_sizeof()
