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

@support.refcount_test
def test_refleaks_in_decompressor___init__():
    gettotalrefcount = support.get_attribute(sys, 'gettotalrefcount')
    lzd = LZMADecompressor()
    refs_before = gettotalrefcount()
    for i in range(100):
        lzd.__init__()
    CompressorDecompressorTestCase.assertAlmostEqual(gettotalrefcount() - refs_before, 0, delta=10)

CompressorDecompressorTestCase = test_lzma.CompressorDecompressorTestCase()
test_refleaks_in_decompressor___init__()
