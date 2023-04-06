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

def test_decompressor_inputbuf_1():
    lzd = LZMADecompressor()
    out = []
    CompressorDecompressorTestCase.assertEqual(lzd.decompress(COMPRESSED_XZ[:100], max_length=0), b'')
    out.append(lzd.decompress(b'', 2))
    out.append(lzd.decompress(COMPRESSED_XZ[100:105], 15))
    out.append(lzd.decompress(COMPRESSED_XZ[105:]))
    CompressorDecompressorTestCase.assertEqual(b''.join(out), INPUT)

CompressorDecompressorTestCase = test_lzma.CompressorDecompressorTestCase()
test_decompressor_inputbuf_1()
