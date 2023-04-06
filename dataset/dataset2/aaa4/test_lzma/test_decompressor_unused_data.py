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

def test_decompressor_unused_data():
    lzd = LZMADecompressor()
    extra = b'fooblibar'
    CompressorDecompressorTestCase._test_decompressor(lzd, COMPRESSED_XZ + extra, lzma.CHECK_CRC64, unused_data=extra)

CompressorDecompressorTestCase = test_lzma.CompressorDecompressorTestCase()
test_decompressor_unused_data()
