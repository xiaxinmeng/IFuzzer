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

def test_with_open():
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'wb') as f:
        f.write(b'xxx')
    f = test_gzip.gzip.GzipFile(TestGzip.filename, 'rb')
    f.close()
    try:
        with f:
            pass
    except ValueError:
        pass
    else:
        TestGzip.fail("__enter__ on a closed file didn't raise an exception")
    try:
        with test_gzip.gzip.GzipFile(TestGzip.filename, 'wb') as f:
            1 / 0
    except ZeroDivisionError:
        pass
    else:
        TestGzip.fail("1/0 didn't raise an exception")

TestGzip = test_gzip.TestGzip()
test_with_open()
