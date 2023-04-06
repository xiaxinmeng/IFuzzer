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

def test_init_mode():
    with TempFile(TESTFN):
        with LZMAFile(TESTFN, 'r'):
            pass
        with LZMAFile(TESTFN, 'rb'):
            pass
        with LZMAFile(TESTFN, 'w'):
            pass
        with LZMAFile(TESTFN, 'wb'):
            pass
        with LZMAFile(TESTFN, 'a'):
            pass
        with LZMAFile(TESTFN, 'ab'):
            pass

FileTestCase = test_lzma.FileTestCase()
test_init_mode()
