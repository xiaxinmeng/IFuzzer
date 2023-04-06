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

def test_empty_flush():
    co = test_zlib.zlib.compressobj(test_zlib.zlib.Z_BEST_COMPRESSION)
    CompressObjectTestCase.assertTrue(co.flush())
    dco = test_zlib.zlib.decompressobj()
    CompressObjectTestCase.assertEqual(dco.flush(), b'')

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_empty_flush()
