import io
import locale
import mimetypes
import pathlib
import sys
import unittest.mock
from test import support
from test.support import os_helper
from platform import win32_edition
import test_mimetypes

def test_help_option():
    support.patch(MimetypesCliTestCase, sys, 'argv', [sys.executable, '-h'])
    with support.captured_stdout() as output:
        with MimetypesCliTestCase.assertRaises(SystemExit) as cm:
            mimetypes._main()
    MimetypesCliTestCase.assertIn('Usage: mimetypes.py', output.getvalue())
    MimetypesCliTestCase.assertEqual(cm.exception.code, 0)

MimetypesCliTestCase = test_mimetypes.MimetypesCliTestCase()
test_help_option()
