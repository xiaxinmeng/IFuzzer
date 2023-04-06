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

def test_filter_properties_roundtrip():
    spec1 = lzma._decode_filter_properties(lzma.FILTER_LZMA1, b']\x00\x00\x80\x00')
    reencoded = lzma._encode_filter_properties(spec1)
    spec2 = lzma._decode_filter_properties(lzma.FILTER_LZMA1, reencoded)
    MiscellaneousTestCase.assertEqual(spec1, spec2)

MiscellaneousTestCase = test_lzma.MiscellaneousTestCase()
test_filter_properties_roundtrip()
