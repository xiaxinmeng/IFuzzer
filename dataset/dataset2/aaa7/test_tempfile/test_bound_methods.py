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

def test_bound_methods():
    f = TestSpooledTemporaryFile.do_create(max_size=30)
    read = f.read
    write = f.write
    seek = f.seek
    write(b'a' * 35)
    write(b'b' * 35)
    seek(0, 0)
    TestSpooledTemporaryFile.assertEqual(read(70), b'a' * 35 + b'b' * 35)

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_bound_methods()
