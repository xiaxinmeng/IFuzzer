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

def test_seek_past_start():
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        f.seek(-88)
        FileTestCase.assertEqual(f.tell(), 0)
        FileTestCase.assertEqual(f.read(), INPUT)

FileTestCase = test_lzma.FileTestCase()
test_seek_past_start()
