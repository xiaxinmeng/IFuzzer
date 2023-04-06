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

def test_readable():
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    try:
        FileTestCase.assertTrue(f.readable())
        f.read()
        FileTestCase.assertTrue(f.readable())
    finally:
        f.close()
    FileTestCase.assertRaises(ValueError, f.readable)
    f = LZMAFile(BytesIO(), 'w')
    try:
        FileTestCase.assertFalse(f.readable())
    finally:
        f.close()
    FileTestCase.assertRaises(ValueError, f.readable)

FileTestCase = test_lzma.FileTestCase()
test_readable()
