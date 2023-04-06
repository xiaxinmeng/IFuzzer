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

def test_encoding_error_handler():
    with test_gzip.gzip.open(TestOpen.filename, 'wb') as f:
        f.write(b'foo\xffbar')
    with test_gzip.gzip.open(TestOpen.filename, 'rt', encoding='ascii', errors='ignore') as f:
        TestOpen.assertEqual(f.read(), 'foobar')

TestOpen = test_gzip.TestOpen()
test_encoding_error_handler()
