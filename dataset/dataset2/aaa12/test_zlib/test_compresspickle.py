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

def test_compresspickle():
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with CompressObjectTestCase.assertRaises((TypeError, pickle.PicklingError)):
            pickle.dumps(test_zlib.zlib.compressobj(test_zlib.zlib.Z_BEST_COMPRESSION), proto)

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_compresspickle()
