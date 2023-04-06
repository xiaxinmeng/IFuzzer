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

def test_properties():
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'x' * 10)
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f.mode, 'w+b')
    TestSpooledTemporaryFile.assertIsNone(f.name)
    with TestSpooledTemporaryFile.assertRaises(AttributeError):
        f.newlines
    with TestSpooledTemporaryFile.assertRaises(AttributeError):
        f.encoding
    with TestSpooledTemporaryFile.assertRaises(AttributeError):
        f.errors
    f.write(b'x')
    TestSpooledTemporaryFile.assertTrue(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f.mode, 'rb+')
    TestSpooledTemporaryFile.assertIsNotNone(f.name)
    with TestSpooledTemporaryFile.assertRaises(AttributeError):
        f.newlines
    with TestSpooledTemporaryFile.assertRaises(AttributeError):
        f.encoding
    with TestSpooledTemporaryFile.assertRaises(AttributeError):
        f.errors

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_properties()
