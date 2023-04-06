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

def test_mtime():
    mtime = 123456789
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'w', mtime=mtime) as fWrite:
        fWrite.write(test_gzip.data1)
    with test_gzip.gzip.GzipFile(TestGzip.filename) as fRead:
        TestGzip.assertTrue(hasattr(fRead, 'mtime'))
        TestGzip.assertIsNone(fRead.mtime)
        dataRead = fRead.read()
        TestGzip.assertEqual(dataRead, test_gzip.data1)
        TestGzip.assertEqual(fRead.mtime, mtime)

TestGzip = test_gzip.TestGzip()
test_mtime()
