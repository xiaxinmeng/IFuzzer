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

def test_decompress_infile_outfile_error():
    (rc, out, err) = assert_python_ok('-m', 'gzip', '-d', 'thisisatest.out')
    TestCommandLine.assertIn(b"filename doesn't end in .gz:", out)
    TestCommandLine.assertEqual(rc, 0)
    TestCommandLine.assertEqual(err, b'')

TestCommandLine = test_gzip.TestCommandLine()
test_decompress_infile_outfile_error()
