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

def test_exclusive_write():
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'xb') as f:
        f.write(test_gzip.data1 * 50)
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'rb') as f:
        TestGzip.assertEqual(f.read(), test_gzip.data1 * 50)
    with TestGzip.assertRaises(FileExistsError):
        test_gzip.gzip.GzipFile(TestGzip.filename, 'xb')

TestGzip = test_gzip.TestGzip()
test_exclusive_write()
