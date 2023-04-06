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

def test_decompress_eof():
    x = b'x\x9cK\xcb\xcf\x07\x00\x02\x82\x01E'
    dco = test_zlib.zlib.decompressobj()
    CompressObjectTestCase.assertFalse(dco.eof)
    dco.decompress(x[:-5])
    CompressObjectTestCase.assertFalse(dco.eof)
    dco.decompress(x[-5:])
    CompressObjectTestCase.assertTrue(dco.eof)
    dco.flush()
    CompressObjectTestCase.assertTrue(dco.eof)

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_decompress_eof()
