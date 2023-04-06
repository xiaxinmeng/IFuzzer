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

def test_decompress_limited():
    """Decompressed data buffering should be limited"""
    bomb = lzma.compress(b'\x00' * int(2000000.0), preset=6)
    FileTestCase.assertLess(len(bomb), _compression.BUFFER_SIZE)
    decomp = LZMAFile(BytesIO(bomb))
    FileTestCase.assertEqual(decomp.read(1), b'\x00')
    max_decomp = 1 + DEFAULT_BUFFER_SIZE
    FileTestCase.assertLessEqual(decomp._buffer.raw.tell(), max_decomp, 'Excessive amount of data was decompressed')

FileTestCase = test_lzma.FileTestCase()
test_decompress_limited()
