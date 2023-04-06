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

@bigmemtest(size=_4G, memuse=1)
def test_read_large(TestGzip, size):
    compressed = test_gzip.gzip.compress(test_gzip.data1, compresslevel=1)
    f = test_gzip.gzip.GzipFile(fileobj=io.BytesIO(compressed), mode='rb')
    TestGzip.assertEqual(f.read(size), test_gzip.data1)

TestGzip = test_gzip.TestGzip()
test_read_large()
