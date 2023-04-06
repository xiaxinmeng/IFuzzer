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

def test_crc32empty():
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(b'', 0), 0)
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(b'', 1), 1)
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(b'', 432), 432)

ChecksumTestCase = test_zlib.ChecksumTestCase()
test_crc32empty()
