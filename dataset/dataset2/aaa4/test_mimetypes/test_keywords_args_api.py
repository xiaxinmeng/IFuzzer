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

def test_keywords_args_api():
    MimeTypesTestCase.assertEqual(MimeTypesTestCase.db.guess_type(url='foo.html', strict=True), ('text/html', None))
    MimeTypesTestCase.assertEqual(MimeTypesTestCase.db.guess_all_extensions(type='image/jpg', strict=True), [])
    MimeTypesTestCase.assertEqual(MimeTypesTestCase.db.guess_extension(type='image/jpg', strict=False), '.jpg')

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
MimeTypesTestCase.setUp()
test_keywords_args_api()
