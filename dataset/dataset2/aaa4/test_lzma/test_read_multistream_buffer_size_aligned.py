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

def test_read_multistream_buffer_size_aligned():
    saved_buffer_size = _compression.BUFFER_SIZE
    _compression.BUFFER_SIZE = len(COMPRESSED_XZ)
    try:
        with LZMAFile(BytesIO(COMPRESSED_XZ * 5)) as f:
            FileTestCase.assertEqual(f.read(), INPUT * 5)
    finally:
        _compression.BUFFER_SIZE = saved_buffer_size

FileTestCase = test_lzma.FileTestCase()
test_read_multistream_buffer_size_aligned()
