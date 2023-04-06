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

def test_seek_whence():
    TestGzip.test_write()
    with test_gzip.gzip.GzipFile(TestGzip.filename) as f:
        f.read(10)
        f.seek(10, whence=1)
        y = f.read(10)
    TestGzip.assertEqual(y, test_gzip.data1[20:30])

TestGzip = test_gzip.TestGzip()
test_seek_whence()
