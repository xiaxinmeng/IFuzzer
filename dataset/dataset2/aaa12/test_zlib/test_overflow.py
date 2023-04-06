import unittest
from test import support
from test.support import import_helper
import binascii
import copy
import pickle
import random
import sys
from test.support import bigmemtest, _1G, _4G
import random
import test_zlib

@support.cpython_only
def test_overflow():
    with ExceptionTestCase.assertRaisesRegex(OverflowError, 'int too large'):
        test_zlib.zlib.decompress(b'', 15, sys.maxsize + 1)
    with ExceptionTestCase.assertRaisesRegex(OverflowError, 'int too large'):
        test_zlib.zlib.decompressobj().decompress(b'', sys.maxsize + 1)
    with ExceptionTestCase.assertRaisesRegex(OverflowError, 'int too large'):
        test_zlib.zlib.decompressobj().flush(sys.maxsize + 1)

ExceptionTestCase = test_zlib.ExceptionTestCase()
test_overflow()
