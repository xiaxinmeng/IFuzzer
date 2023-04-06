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

def test_buffered_reader():
    TestGzip.test_write()
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'rb') as f:
        with io.BufferedReader(f) as r:
            lines = [line for line in r]
    TestGzip.assertEqual(lines, 50 * test_gzip.data1.splitlines(keepends=True))

TestGzip = test_gzip.TestGzip()
test_buffered_reader()
