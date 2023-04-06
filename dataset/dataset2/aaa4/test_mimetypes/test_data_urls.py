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

def test_data_urls():
    eq = MimeTypesTestCase.assertEqual
    guess_type = MimeTypesTestCase.db.guess_type
    eq(guess_type('data:invalidDataWithoutComma'), (None, None))
    eq(guess_type('data:,thisIsTextPlain'), ('text/plain', None))
    eq(guess_type('data:;base64,thisIsTextPlain'), ('text/plain', None))
    eq(guess_type('data:text/x-foo,thisIsTextXFoo'), ('text/x-foo', None))

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
MimeTypesTestCase.setUp()
test_data_urls()
