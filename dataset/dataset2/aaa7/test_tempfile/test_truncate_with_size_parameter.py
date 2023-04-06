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

def test_truncate_with_size_parameter():
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'abcdefg\n')
    f.seek(0)
    f.truncate()
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f._file.getvalue(), b'')
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'abcdefg\n')
    f.truncate(4)
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f._file.getvalue(), b'abcd')
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'abcdefg\n')
    f.truncate(20)
    TestSpooledTemporaryFile.assertTrue(f._rolled)
    TestSpooledTemporaryFile.assertEqual(os.fstat(f.fileno()).st_size, 20)

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_truncate_with_size_parameter()
