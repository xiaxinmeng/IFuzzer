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

def test_newline():
    uncompressed = test_gzip.data1.decode('ascii') * 50
    with test_gzip.gzip.open(TestOpen.filename, 'wt', newline='\n') as f:
        f.write(uncompressed)
    with test_gzip.gzip.open(TestOpen.filename, 'rt', newline='\r') as f:
        TestOpen.assertEqual(f.readlines(), [uncompressed])

TestOpen = test_gzip.TestOpen()
test_newline()
