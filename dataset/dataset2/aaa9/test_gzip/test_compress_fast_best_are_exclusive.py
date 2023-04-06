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

def test_compress_fast_best_are_exclusive():
    (rc, out, err) = assert_python_failure('-m', 'gzip', '--fast', '--best')
    TestCommandLine.assertIn(b'error: argument --best: not allowed with argument --fast', err)
    TestCommandLine.assertEqual(out, b'')

TestCommandLine = test_gzip.TestCommandLine()
test_compress_fast_best_are_exclusive()
