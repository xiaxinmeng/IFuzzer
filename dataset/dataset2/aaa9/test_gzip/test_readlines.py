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

def test_readlines():
    TestGzip.test_write()
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'rb') as f:
        L = f.readlines()
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'rb') as f:
        while 1:
            L = f.readlines(150)
            if L == []:
                break

TestGzip = test_gzip.TestGzip()
test_readlines()
