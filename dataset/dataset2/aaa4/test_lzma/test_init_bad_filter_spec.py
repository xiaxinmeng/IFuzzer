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

def test_init_bad_filter_spec():
    with FileTestCase.assertRaises(TypeError):
        LZMAFile(BytesIO(), 'w', filters=[b'wobsite'])
    with FileTestCase.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'xyzzy': 3}])
    with FileTestCase.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': 98765}])
    with FileTestCase.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': lzma.FILTER_LZMA2, 'foo': 0}])
    with FileTestCase.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': lzma.FILTER_DELTA, 'foo': 0}])
    with FileTestCase.assertRaises(ValueError):
        LZMAFile(BytesIO(), 'w', filters=[{'id': lzma.FILTER_X86, 'foo': 0}])

FileTestCase = test_lzma.FileTestCase()
test_init_bad_filter_spec()
