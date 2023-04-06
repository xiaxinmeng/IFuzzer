import _compression
from io import BytesIO, UnsupportedOperation, DEFAULT_BUFFER_SIZE
import os
import pathlib
import pickle
import random
import sys
from test import support
import unittest
from test.support import _4G, bigmemtest, run_unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink
from lzma import LZMACompressor, LZMADecompressor, LZMAError, LZMAFile
import test_lzma

def test__encode_filter_properties():
    with MiscellaneousTestCase.assertRaises(TypeError):
        lzma._encode_filter_properties(b'not a dict')
    with MiscellaneousTestCase.assertRaises(ValueError):
        lzma._encode_filter_properties({'id': 256})
    with MiscellaneousTestCase.assertRaises(ValueError):
        lzma._encode_filter_properties({'id': lzma.FILTER_LZMA2, 'junk': 12})
    with MiscellaneousTestCase.assertRaises(lzma.LZMAError):
        lzma._encode_filter_properties({'id': lzma.FILTER_DELTA, 'dist': 9001})
    props = lzma._encode_filter_properties({'id': lzma.FILTER_LZMA1, 'pb': 2, 'lp': 0, 'lc': 3, 'dict_size': 8 << 20})
    MiscellaneousTestCase.assertEqual(props, b']\x00\x00\x80\x00')

MiscellaneousTestCase = test_lzma.MiscellaneousTestCase()
test__encode_filter_properties()
