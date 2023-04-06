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

def test_pathlike_file():
    filename = pathlib.Path(TestOpen.filename)
    with test_gzip.gzip.open(filename, 'wb') as f:
        f.write(test_gzip.data1 * 50)
    with test_gzip.gzip.open(filename, 'ab') as f:
        f.write(test_gzip.data1)
    with test_gzip.gzip.open(filename) as f:
        TestOpen.assertEqual(f.read(), test_gzip.data1 * 51)

TestOpen = test_gzip.TestOpen()
test_pathlike_file()
