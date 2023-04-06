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

def test_init_with_filename():
    with TempFile(TESTFN, COMPRESSED_XZ):
        with LZMAFile(TESTFN) as f:
            pass
        with LZMAFile(TESTFN, 'w') as f:
            pass
        with LZMAFile(TESTFN, 'a') as f:
            pass

FileTestCase = test_lzma.FileTestCase()
test_init_with_filename()
