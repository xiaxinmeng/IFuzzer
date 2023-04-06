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

def test_flush_custom_length():
    input = test_zlib.HAMLET_SCENE * 10
    data = test_zlib.zlib.compress(input, 1)
    dco = test_zlib.zlib.decompressobj()
    dco.decompress(data, 1)
    CompressObjectTestCase.assertEqual(dco.flush(test_zlib.CustomInt()), input[1:])

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_flush_custom_length()
