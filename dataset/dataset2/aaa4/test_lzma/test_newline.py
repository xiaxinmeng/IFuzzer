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

def test_newline():
    text = INPUT.decode('ascii')
    with BytesIO() as bio:
        with lzma.open(bio, 'wt', newline='\n') as f:
            f.write(text)
        bio.seek(0)
        with lzma.open(bio, 'rt', newline='\r') as f:
            OpenTestCase.assertEqual(f.readlines(), [text])

OpenTestCase = test_lzma.OpenTestCase()
test_newline()
