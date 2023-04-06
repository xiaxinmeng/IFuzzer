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

def test_init():
    with LZMAFile(BytesIO(COMPRESSED_XZ)) as f:
        pass
    with LZMAFile(BytesIO(), 'w') as f:
        pass
    with LZMAFile(BytesIO(), 'x') as f:
        pass
    with LZMAFile(BytesIO(), 'a') as f:
        pass

FileTestCase = test_lzma.FileTestCase()
test_init()
