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

def test_maxlenmisc():
    dco = test_zlib.zlib.decompressobj()
    CompressObjectTestCase.assertRaises(ValueError, dco.decompress, b'', -1)
    CompressObjectTestCase.assertEqual(b'', dco.unconsumed_tail)

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_maxlenmisc()
