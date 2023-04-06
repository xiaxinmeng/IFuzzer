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

@test_zlib.requires_Decompress_copy
def test_baddecompresscopy():
    data = test_zlib.zlib.compress(test_zlib.HAMLET_SCENE)
    d = test_zlib.zlib.decompressobj()
    d.decompress(data)
    d.flush()
    CompressObjectTestCase.assertRaises(ValueError, d.copy)
    CompressObjectTestCase.assertRaises(ValueError, copy.copy, d)
    CompressObjectTestCase.assertRaises(ValueError, copy.deepcopy, d)

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_baddecompresscopy()
