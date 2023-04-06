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

def test_custom_bufsize():
    data = test_zlib.HAMLET_SCENE * 10
    compressed = test_zlib.zlib.compress(data, 1)
    CompressTestCase.assertEqual(test_zlib.zlib.decompress(compressed, 15, test_zlib.CustomInt()), data)

CompressTestCase = test_zlib.CompressTestCase()
test_custom_bufsize()
