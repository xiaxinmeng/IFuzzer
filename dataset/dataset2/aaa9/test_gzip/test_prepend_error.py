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

def test_prepend_error():
    with test_gzip.gzip.open(TestGzip.filename, 'wb') as f:
        f.write(test_gzip.data1)
    with test_gzip.gzip.open(TestGzip.filename, 'rb') as f:
        f._buffer.raw._fp.prepend()

TestGzip = test_gzip.TestGzip()
test_prepend_error()
