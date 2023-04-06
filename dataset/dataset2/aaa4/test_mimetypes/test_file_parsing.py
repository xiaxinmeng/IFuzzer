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

def test_file_parsing():
    eq = MimeTypesTestCase.assertEqual
    sio = io.StringIO('x-application/x-unittest pyunit\n')
    MimeTypesTestCase.db.readfp(sio)
    eq(MimeTypesTestCase.db.guess_type('foo.pyunit'), ('x-application/x-unittest', None))
    eq(MimeTypesTestCase.db.guess_extension('x-application/x-unittest'), '.pyunit')

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
MimeTypesTestCase.setUp()
test_file_parsing()
