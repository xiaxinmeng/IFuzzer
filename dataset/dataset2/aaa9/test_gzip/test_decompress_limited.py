import array
import functools
import io
import os
import pathlib
import struct
import sys
import unittest
from subprocess import PIPE, Popen
from test import support
from test.support import import_helper
from test.support import os_helper
from test.support import _4G, bigmemtest
from test.support.script_helper import assert_python_ok, assert_python_failure
import test_gzip

def test_decompress_limited():
    """Decompressed data buffering should be limited"""
    bomb = test_gzip.gzip.compress(b'\x00' * int(2000000.0), compresslevel=9)
    TestGzip.assertLess(len(bomb), io.DEFAULT_BUFFER_SIZE)
    bomb = io.BytesIO(bomb)
    decomp = test_gzip.gzip.GzipFile(fileobj=bomb)
    TestGzip.assertEqual(decomp.read(1), b'\x00')
    max_decomp = 1 + io.DEFAULT_BUFFER_SIZE
    TestGzip.assertLessEqual(decomp._buffer.raw.tell(), max_decomp, 'Excessive amount of data was decompressed')

TestGzip = test_gzip.TestGzip()
test_decompress_limited()
