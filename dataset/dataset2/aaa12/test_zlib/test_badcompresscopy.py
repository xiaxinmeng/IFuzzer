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

@test_zlib.requires_Compress_copy
def test_badcompresscopy():
    c = test_zlib.zlib.compressobj()
    c.compress(test_zlib.HAMLET_SCENE)
    c.flush()
    CompressObjectTestCase.assertRaises(ValueError, c.copy)
    CompressObjectTestCase.assertRaises(ValueError, copy.copy, c)
    CompressObjectTestCase.assertRaises(ValueError, copy.deepcopy, c)

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_badcompresscopy()
