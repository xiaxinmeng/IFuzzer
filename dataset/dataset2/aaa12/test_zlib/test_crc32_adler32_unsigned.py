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

def test_crc32_adler32_unsigned():
    foo = b'abcdefghijklmnop'
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(foo), 2486878355)
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(b'spam'), 1138425661)
    ChecksumTestCase.assertEqual(test_zlib.zlib.adler32(foo + foo), 3573550353)
    ChecksumTestCase.assertEqual(test_zlib.zlib.adler32(b'spam'), 72286642)

ChecksumTestCase = test_zlib.ChecksumTestCase()
test_crc32_adler32_unsigned()
