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

def test_decompress_cannot_have_flags_compression():
    (rc, out, err) = assert_python_failure('-m', 'gzip', '--fast', '-d')
    TestCommandLine.assertIn(b'error: argument -d/--decompress: not allowed with argument --fast', err)
    TestCommandLine.assertEqual(out, b'')

TestCommandLine = test_gzip.TestCommandLine()
test_decompress_cannot_have_flags_compression()
