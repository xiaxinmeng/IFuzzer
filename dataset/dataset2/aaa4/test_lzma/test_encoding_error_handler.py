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

def test_encoding_error_handler():
    with BytesIO(lzma.compress(b'foo\xffbar')) as bio:
        with lzma.open(bio, 'rt', encoding='ascii', errors='ignore') as f:
            OpenTestCase.assertEqual(f.read(), 'foobar')

OpenTestCase = test_lzma.OpenTestCase()
test_encoding_error_handler()
