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

def test_maxlen_large():
    data = test_zlib.HAMLET_SCENE * 10
    CompressObjectTestCase.assertGreater(len(data), test_zlib.zlib.DEF_BUF_SIZE)
    compressed = test_zlib.zlib.compress(data, 1)
    dco = test_zlib.zlib.decompressobj()
    CompressObjectTestCase.assertEqual(dco.decompress(compressed, sys.maxsize), data)

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_maxlen_large()
