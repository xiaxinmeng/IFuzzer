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

def test_text_mode():
    f = tempfile.SpooledTemporaryFile(mode='w+', max_size=10, encoding='utf-8')
    f.write('abc\n')
    f.seek(0)
    TestSpooledTemporaryFile.assertEqual(f.read(), 'abc\n')
    f.write('def\n')
    f.seek(0)
    TestSpooledTemporaryFile.assertEqual(f.read(), 'abc\ndef\n')
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f.mode, 'w+')
    TestSpooledTemporaryFile.assertIsNone(f.name)
    TestSpooledTemporaryFile.assertEqual(f.newlines, os.linesep)
    TestSpooledTemporaryFile.assertEqual(f.encoding, 'utf-8')
    TestSpooledTemporaryFile.assertEqual(f.errors, 'strict')
    f.write('xyzzy\n')
    f.seek(0)
    TestSpooledTemporaryFile.assertEqual(f.read(), 'abc\ndef\nxyzzy\n')
    f.write('foo\x1abar\n')
    f.seek(0)
    TestSpooledTemporaryFile.assertEqual(f.read(), 'abc\ndef\nxyzzy\nfoo\x1abar\n')
    TestSpooledTemporaryFile.assertTrue(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f.mode, 'w+')
    TestSpooledTemporaryFile.assertIsNotNone(f.name)
    TestSpooledTemporaryFile.assertEqual(f.newlines, os.linesep)
    TestSpooledTemporaryFile.assertEqual(f.encoding, 'utf-8')
    TestSpooledTemporaryFile.assertEqual(f.errors, 'strict')

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_text_mode()
