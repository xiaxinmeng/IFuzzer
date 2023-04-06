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

def test_seek_backward():
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        f.read(1001)
        f.seek(211)
        FileTestCase.assertEqual(f.read(), INPUT[211:])

FileTestCase = test_lzma.FileTestCase()
test_seek_backward()
