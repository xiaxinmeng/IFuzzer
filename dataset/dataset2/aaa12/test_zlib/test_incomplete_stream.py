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

def test_incomplete_stream():
    x = test_zlib.zlib.compress(test_zlib.HAMLET_SCENE)
    CompressTestCase.assertRaisesRegex(test_zlib.zlib.error, 'Error -5 while decompressing data: incomplete or truncated stream', test_zlib.zlib.decompress, x[:-1])

CompressTestCase = test_zlib.CompressTestCase()
test_incomplete_stream()
