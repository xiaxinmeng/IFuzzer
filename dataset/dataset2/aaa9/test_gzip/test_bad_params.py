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

def test_bad_params():
    with TestOpen.assertRaises(TypeError):
        test_gzip.gzip.open(123.456)
    with TestOpen.assertRaises(ValueError):
        test_gzip.gzip.open(TestOpen.filename, 'wbt')
    with TestOpen.assertRaises(ValueError):
        test_gzip.gzip.open(TestOpen.filename, 'xbt')
    with TestOpen.assertRaises(ValueError):
        test_gzip.gzip.open(TestOpen.filename, 'rb', encoding='utf-8')
    with TestOpen.assertRaises(ValueError):
        test_gzip.gzip.open(TestOpen.filename, 'rb', errors='ignore')
    with TestOpen.assertRaises(ValueError):
        test_gzip.gzip.open(TestOpen.filename, 'rb', newline='\n')

TestOpen = test_gzip.TestOpen()
test_bad_params()
