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

def test_badcompressobj():
    ExceptionTestCase.assertRaises(ValueError, test_zlib.zlib.compressobj, 1, test_zlib.zlib.DEFLATED, 0)
    ExceptionTestCase.assertRaises(ValueError, test_zlib.zlib.compressobj, 1, test_zlib.zlib.DEFLATED, test_zlib.zlib.MAX_WBITS + 1)

ExceptionTestCase = test_zlib.ExceptionTestCase()
test_badcompressobj()
