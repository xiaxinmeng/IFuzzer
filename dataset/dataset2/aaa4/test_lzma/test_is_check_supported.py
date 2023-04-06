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

def test_is_check_supported():
    MiscellaneousTestCase.assertTrue(lzma.is_check_supported(lzma.CHECK_NONE))
    MiscellaneousTestCase.assertTrue(lzma.is_check_supported(lzma.CHECK_CRC32))
    MiscellaneousTestCase.assertFalse(lzma.is_check_supported(lzma.CHECK_ID_MAX + 1))
    MiscellaneousTestCase.assertFalse(lzma.is_check_supported(lzma.CHECK_UNKNOWN))

MiscellaneousTestCase = test_lzma.MiscellaneousTestCase()
test_is_check_supported()
