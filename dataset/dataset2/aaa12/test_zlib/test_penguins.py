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

def test_penguins():
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(b'penguin', 0), 3854672160)
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(b'penguin', 1), 1136044692)
    ChecksumTestCase.assertEqual(test_zlib.zlib.adler32(b'penguin', 0), 198116086)
    ChecksumTestCase.assertEqual(test_zlib.zlib.adler32(b'penguin', 1), 198574839)
    ChecksumTestCase.assertEqual(test_zlib.zlib.crc32(b'penguin'), test_zlib.zlib.crc32(b'penguin', 0))
    ChecksumTestCase.assertEqual(test_zlib.zlib.adler32(b'penguin'), test_zlib.zlib.adler32(b'penguin', 1))

ChecksumTestCase = test_zlib.ChecksumTestCase()
test_penguins()
