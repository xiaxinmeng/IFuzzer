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

def test_read_with_extra():
    gzdata = b'\x1f\x8b\x08\x04\xb2\x17cQ\x02\xff\x05\x00Extra\x0bI-.\x01\x002\xd1Mx\x04\x00\x00\x00'
    with test_gzip.gzip.GzipFile(fileobj=io.BytesIO(gzdata)) as f:
        TestGzip.assertEqual(f.read(), b'Test')

TestGzip = test_gzip.TestGzip()
test_read_with_extra()
