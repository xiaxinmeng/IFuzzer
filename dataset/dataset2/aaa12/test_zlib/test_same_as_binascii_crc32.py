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

def test_same_as_binascii_crc32():
    foo = b'abcdefghijklmnop'
    crc = 2486878355
    ChecksumTestCase.assertEqual(binascii.crc32(foo), crc)
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(foo), crc)
    ChecksumTestCase.assertEqual(binascii.crc32(b'spam'), test_zlib.zlib.crc32(b'spam'))

ChecksumTestCase = test_zlib.ChecksumTestCase()
test_same_as_binascii_crc32()
