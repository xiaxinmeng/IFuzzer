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

def test_speech():
    x = test_zlib.zlib.compress(test_zlib.HAMLET_SCENE)
    CompressTestCase.assertEqual(test_zlib.zlib.decompress(x), test_zlib.HAMLET_SCENE)

CompressTestCase = test_zlib.CompressTestCase()
test_speech()
