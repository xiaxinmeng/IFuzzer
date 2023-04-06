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

def test_default_data():
    eq = MimeTypesTestCase.assertEqual
    eq(MimeTypesTestCase.db.guess_type('foo.html'), ('text/html', None))
    eq(MimeTypesTestCase.db.guess_type('foo.HTML'), ('text/html', None))
    eq(MimeTypesTestCase.db.guess_type('foo.tgz'), ('application/x-tar', 'gzip'))
    eq(MimeTypesTestCase.db.guess_type('foo.tar.gz'), ('application/x-tar', 'gzip'))
    eq(MimeTypesTestCase.db.guess_type('foo.tar.Z'), ('application/x-tar', 'compress'))
    eq(MimeTypesTestCase.db.guess_type('foo.tar.bz2'), ('application/x-tar', 'bzip2'))
    eq(MimeTypesTestCase.db.guess_type('foo.tar.xz'), ('application/x-tar', 'xz'))

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
MimeTypesTestCase.setUp()
test_default_data()
