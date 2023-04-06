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

def test_write_incompatible_type():
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'wb') as f:
        with TestGzip.assertRaises(TypeError):
            f.write('')
        with TestGzip.assertRaises(TypeError):
            f.write([])
        f.write(test_gzip.data1)
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'rb') as f:
        TestGzip.assertEqual(f.read(), test_gzip.data1)

TestGzip = test_gzip.TestGzip()
test_write_incompatible_type()
