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

def test_decompress_incomplete_stream():
    x = b'x\x9cK\xcb\xcf\x07\x00\x02\x82\x01E'
    CompressObjectTestCase.assertEqual(test_zlib.zlib.decompress(x), b'foo')
    CompressObjectTestCase.assertRaises(test_zlib.zlib.error, test_zlib.zlib.decompress, x[:-5])
    dco = test_zlib.zlib.decompressobj()
    y = dco.decompress(x[:-5])
    y += dco.flush()
    CompressObjectTestCase.assertEqual(y, b'foo')

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_decompress_incomplete_stream()
