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

def test_pickle():
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with CompressorDecompressorTestCase.assertRaises(TypeError):
            pickle.dumps(LZMACompressor(), proto)
        with CompressorDecompressorTestCase.assertRaises(TypeError):
            pickle.dumps(LZMADecompressor(), proto)

CompressorDecompressorTestCase = test_lzma.CompressorDecompressorTestCase()
test_pickle()
