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

def test_read_0():
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        FileTestCase.assertEqual(f.read(0), b'')
    with LZMAFile(BytesIO(COMPRESSED_ALONE)) as f:
        FileTestCase.assertEqual(f.read(0), b'')
    with LZMAFile(BytesIO(COMPRESSED_XZ), format=lzma.FORMAT_XZ) as f:
        FileTestCase.assertEqual(f.read(0), b'')
    with LZMAFile(BytesIO(COMPRESSED_ALONE), format=lzma.FORMAT_ALONE) as f:
        FileTestCase.assertEqual(f.read(0), b'')

FileTestCase = test_lzma.FileTestCase()
test_read_0()
