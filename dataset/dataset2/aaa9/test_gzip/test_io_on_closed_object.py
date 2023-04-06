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

def test_io_on_closed_object():
    TestGzip.test_write()
    f = test_gzip.gzip.GzipFile(TestGzip.filename, 'r')
    fileobj = f.fileobj
    TestGzip.assertFalse(fileobj.closed)
    f.close()
    TestGzip.assertTrue(fileobj.closed)
    with TestGzip.assertRaises(ValueError):
        f.read(1)
    with TestGzip.assertRaises(ValueError):
        f.seek(0)
    with TestGzip.assertRaises(ValueError):
        f.tell()
    f = test_gzip.gzip.GzipFile(TestGzip.filename, 'w')
    fileobj = f.fileobj
    TestGzip.assertFalse(fileobj.closed)
    f.close()
    TestGzip.assertTrue(fileobj.closed)
    with TestGzip.assertRaises(ValueError):
        f.write(b'')
    with TestGzip.assertRaises(ValueError):
        f.flush()

TestGzip = test_gzip.TestGzip()
test_io_on_closed_object()
