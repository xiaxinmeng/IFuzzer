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

def test_write_sequential():
    f = TestSpooledTemporaryFile.do_create(max_size=30)
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    f.write(b'x' * 20)
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    f.write(b'x' * 10)
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    f.write(b'x')
    TestSpooledTemporaryFile.assertTrue(f._rolled)

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_write_sequential()
