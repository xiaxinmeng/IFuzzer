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

def test_decompress_memlimit():
    with CompressDecompressFunctionTestCase.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_XZ, memlimit=1024)
    with CompressDecompressFunctionTestCase.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_XZ, format=lzma.FORMAT_XZ, memlimit=1024)
    with CompressDecompressFunctionTestCase.assertRaises(LZMAError):
        lzma.decompress(COMPRESSED_ALONE, format=lzma.FORMAT_ALONE, memlimit=1024)

CompressDecompressFunctionTestCase = test_lzma.CompressDecompressFunctionTestCase()
test_decompress_memlimit()
