import tempfile
import errno
import io
import os
import pathlib
import sys
import re
import warnings
import contextlib
import stat
import types
import weakref
from unittest import mock
import unittest
from test import support
from test.support import os_helper
from test.support import script_helper
from test.support import warnings_helper
import test_tempfile

def test_method_lookup():
    f = TestNamedTemporaryFile.do_create()
    wr = weakref.ref(f)
    write = f.write
    write2 = f.write
    del f
    write(b'foo')
    del write
    write2(b'bar')
    del write2
    if support.check_impl_detail(cpython=True):
        TestNamedTemporaryFile.assertIsNone(wr())

TestNamedTemporaryFile = test_tempfile.TestNamedTemporaryFile()
test_method_lookup()
