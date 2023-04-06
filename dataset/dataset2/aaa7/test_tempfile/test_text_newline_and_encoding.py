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

def test_text_newline_and_encoding():
    f = tempfile.SpooledTemporaryFile(mode='w+', max_size=10, newline='', encoding='utf-8', errors='ignore')
    f.write('Λ\r\n')
    f.seek(0)
    TestSpooledTemporaryFile.assertEqual(f.read(), 'Λ\r\n')
    TestSpooledTemporaryFile.assertFalse(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f.mode, 'w+')
    TestSpooledTemporaryFile.assertIsNone(f.name)
    TestSpooledTemporaryFile.assertIsNotNone(f.newlines)
    TestSpooledTemporaryFile.assertEqual(f.encoding, 'utf-8')
    TestSpooledTemporaryFile.assertEqual(f.errors, 'ignore')
    f.write('Μ' * 10 + '\r\n')
    f.write('Ν' * 20)
    f.seek(0)
    TestSpooledTemporaryFile.assertEqual(f.read(), 'Λ\r\n' + 'Μ' * 10 + '\r\n' + 'Ν' * 20)
    TestSpooledTemporaryFile.assertTrue(f._rolled)
    TestSpooledTemporaryFile.assertEqual(f.mode, 'w+')
    TestSpooledTemporaryFile.assertIsNotNone(f.name)
    TestSpooledTemporaryFile.assertIsNotNone(f.newlines)
    TestSpooledTemporaryFile.assertEqual(f.encoding, 'utf-8')
    TestSpooledTemporaryFile.assertEqual(f.errors, 'ignore')

TestSpooledTemporaryFile = test_tempfile.TestSpooledTemporaryFile()
test_text_newline_and_encoding()
