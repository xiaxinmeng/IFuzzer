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

def test_1647484():
    for mode in ('wb', 'rb'):
        with test_gzip.gzip.GzipFile(TestGzip.filename, mode) as f:
            TestGzip.assertTrue(hasattr(f, 'name'))
            TestGzip.assertEqual(f.name, TestGzip.filename)

TestGzip = test_gzip.TestGzip()
test_1647484()
