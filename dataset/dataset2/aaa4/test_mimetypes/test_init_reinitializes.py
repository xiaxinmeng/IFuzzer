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

def test_init_reinitializes():
    mimetypes.add_type('foo/bar', '.foobar')
    MimeTypesTestCase.assertEqual(mimetypes.guess_extension('foo/bar'), '.foobar')
    mimetypes.init()
    MimeTypesTestCase.assertEqual(mimetypes.guess_extension('foo/bar'), None)

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
test_init_reinitializes()
