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

def test__decode_filter_properties():
    with MiscellaneousTestCase.assertRaises(TypeError):
        lzma._decode_filter_properties(lzma.FILTER_X86, {'should be': bytes})
    with MiscellaneousTestCase.assertRaises(lzma.LZMAError):
        lzma._decode_filter_properties(lzma.FILTER_DELTA, b'too long')
    filterspec = lzma._decode_filter_properties(lzma.FILTER_LZMA1, b']\x00\x00\x80\x00')
    MiscellaneousTestCase.assertEqual(filterspec['id'], lzma.FILTER_LZMA1)
    MiscellaneousTestCase.assertEqual(filterspec['pb'], 2)
    MiscellaneousTestCase.assertEqual(filterspec['lp'], 0)
    MiscellaneousTestCase.assertEqual(filterspec['lc'], 3)
    MiscellaneousTestCase.assertEqual(filterspec['dict_size'], 8 << 20)

MiscellaneousTestCase = test_lzma.MiscellaneousTestCase()
test__decode_filter_properties()
