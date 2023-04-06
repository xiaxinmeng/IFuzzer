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

def test_clear_unconsumed_tail():
    cdata = b'x\x9cKLJ\x06\x00\x02M\x01'
    dco = test_zlib.zlib.decompressobj()
    ddata = dco.decompress(cdata, 1)
    ddata += dco.decompress(dco.unconsumed_tail)
    CompressObjectTestCase.assertEqual(dco.unconsumed_tail, b'')

CompressObjectTestCase = test_zlib.CompressObjectTestCase()
test_clear_unconsumed_tail()
