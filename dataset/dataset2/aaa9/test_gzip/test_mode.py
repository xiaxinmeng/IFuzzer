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

def test_mode():
    TestGzip.test_write()
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'r') as f:
        TestGzip.assertEqual(f.myfileobj.mode, 'rb')
    os_helper.unlink(TestGzip.filename)
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'x') as f:
        TestGzip.assertEqual(f.myfileobj.mode, 'xb')

TestGzip = test_gzip.TestGzip()
test_mode()
