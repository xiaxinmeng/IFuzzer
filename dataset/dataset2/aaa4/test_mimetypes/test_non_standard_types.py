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

def test_non_standard_types():
    eq = MimeTypesTestCase.assertEqual
    eq(MimeTypesTestCase.db.guess_type('foo.xul', strict=True), (None, None))
    eq(MimeTypesTestCase.db.guess_extension('image/jpg', strict=True), None)
    eq(MimeTypesTestCase.db.guess_type('foo.xul', strict=False), ('text/xul', None))
    eq(MimeTypesTestCase.db.guess_type('foo.XUL', strict=False), ('text/xul', None))
    eq(MimeTypesTestCase.db.guess_type('foo.invalid', strict=False), (None, None))
    eq(MimeTypesTestCase.db.guess_extension('image/jpg', strict=False), '.jpg')
    eq(MimeTypesTestCase.db.guess_extension('image/JPG', strict=False), '.jpg')

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
MimeTypesTestCase.setUp()
test_non_standard_types()
