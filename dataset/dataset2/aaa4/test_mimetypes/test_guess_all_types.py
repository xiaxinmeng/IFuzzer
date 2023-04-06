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

def test_guess_all_types():
    eq = MimeTypesTestCase.assertEqual
    unless = MimeTypesTestCase.assertTrue
    all = set(MimeTypesTestCase.db.guess_all_extensions('text/plain', strict=True))
    unless(all >= set(['.bat', '.c', '.h', '.ksh', '.pl', '.txt']))
    all = MimeTypesTestCase.db.guess_all_extensions('image/jpg', strict=False)
    all.sort()
    eq(all, ['.jpg'])
    all = MimeTypesTestCase.db.guess_all_extensions('image/jpg', strict=True)
    eq(all, [])

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
MimeTypesTestCase.setUp()
test_guess_all_types()
