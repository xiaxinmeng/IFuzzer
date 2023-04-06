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

def test_textio_readlines():
    lines = (test_gzip.data1 * 50).decode('ascii').splitlines(keepends=True)
    TestGzip.test_write()
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'r') as f:
        with io.TextIOWrapper(f, encoding='ascii') as t:
            TestGzip.assertEqual(t.readlines(), lines)

TestGzip = test_gzip.TestGzip()
test_textio_readlines()
