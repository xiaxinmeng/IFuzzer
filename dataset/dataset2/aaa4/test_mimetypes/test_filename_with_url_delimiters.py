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

def test_filename_with_url_delimiters():
    eq = MimeTypesTestCase.assertEqual
    gzip_expected = ('application/x-tar', 'gzip')
    eq(MimeTypesTestCase.db.guess_type(';1.tar.gz'), gzip_expected)
    eq(MimeTypesTestCase.db.guess_type('?1.tar.gz'), gzip_expected)
    eq(MimeTypesTestCase.db.guess_type('#1.tar.gz'), gzip_expected)
    eq(MimeTypesTestCase.db.guess_type('#1#.tar.gz'), gzip_expected)
    eq(MimeTypesTestCase.db.guess_type(';1#.tar.gz'), gzip_expected)
    eq(MimeTypesTestCase.db.guess_type(';&1=123;?.tar.gz'), gzip_expected)
    eq(MimeTypesTestCase.db.guess_type('?k1=v1&k2=v2.tar.gz'), gzip_expected)
    eq(MimeTypesTestCase.db.guess_type(' \\"\\`;b&b&c |.tar.gz'), gzip_expected)

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
MimeTypesTestCase.setUp()
test_filename_with_url_delimiters()
