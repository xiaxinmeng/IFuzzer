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

def test_closed():
    f = LZMAFile(BytesIO(COMPRESSED_XZ))
    try:
        FileTestCase.assertFalse(f.closed)
        f.read()
        FileTestCase.assertFalse(f.closed)
    finally:
        f.close()
    FileTestCase.assertTrue(f.closed)
    f = LZMAFile(BytesIO(), 'w')
    try:
        FileTestCase.assertFalse(f.closed)
    finally:
        f.close()
    FileTestCase.assertTrue(f.closed)

FileTestCase = test_lzma.FileTestCase()
test_closed()
