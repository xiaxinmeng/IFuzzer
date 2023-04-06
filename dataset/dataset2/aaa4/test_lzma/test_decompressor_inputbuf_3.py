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

def test_decompressor_inputbuf_3():
    lzd = LZMADecompressor()
    out = []
    out.append(lzd.decompress(COMPRESSED_XZ[:200], 5))
    out.append(lzd.decompress(COMPRESSED_XZ[200:300], 5))
    out.append(lzd.decompress(COMPRESSED_XZ[300:]))
    CompressorDecompressorTestCase.assertEqual(b''.join(out), INPUT)

CompressorDecompressorTestCase = test_lzma.CompressorDecompressorTestCase()
test_decompressor_inputbuf_3()
