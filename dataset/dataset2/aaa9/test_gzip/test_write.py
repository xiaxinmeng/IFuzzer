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

def test_write():
    with test_gzip.gzip.GzipFile(TestGzip.filename, 'wb') as f:
        f.write(test_gzip.data1 * 50)
        f.flush()
        f.fileno()
        if hasattr(os, 'fsync'):
            os.fsync(f.fileno())
        f.close()
    f.close()

TestGzip = test_gzip.TestGzip()
test_write()
