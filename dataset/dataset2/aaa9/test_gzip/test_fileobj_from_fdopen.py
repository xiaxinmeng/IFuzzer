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

def test_fileobj_from_fdopen():
    fd = os.open(TestGzip.filename, os.O_WRONLY | os.O_CREAT)
    with os.fdopen(fd, 'wb') as f:
        with test_gzip.gzip.GzipFile(fileobj=f, mode='w') as g:
            pass

TestGzip = test_gzip.TestGzip()
test_fileobj_from_fdopen()
