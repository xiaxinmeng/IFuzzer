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

def test_adler32start():
    ChecksumTestCase.assertEqual(test_zlib.zlib.adler32(b''), test_zlib.zlib.adler32(b'', 1))
    ChecksumTestCase.assertTrue(test_zlib.zlib.adler32(b'abc', 4294967295))

ChecksumTestCase = test_zlib.ChecksumTestCase()
test_adler32start()
