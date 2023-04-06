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

def test_write_memoryview():
    TestGzip.write_and_read_back(memoryview(test_gzip.data1 * 50))
    m = memoryview(bytes(range(256)))
    data = m.cast('B', shape=[8, 8, 4])
    TestGzip.write_and_read_back(data)

TestGzip = test_gzip.TestGzip()
test_write_memoryview()
