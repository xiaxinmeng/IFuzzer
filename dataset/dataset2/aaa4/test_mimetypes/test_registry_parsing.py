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

@unittest.skipIf(win32_edition() in ('NanoServer', 'WindowsCoreHeadless', 'IoTEdgeOS'), 'MIME types registry keys unavailable')
def test_registry_parsing():
    eq = Win32MimeTypesTestCase.assertEqual
    eq(Win32MimeTypesTestCase.db.guess_type('foo.txt'), ('text/plain', None))
    eq(Win32MimeTypesTestCase.db.guess_type('image.jpg'), ('image/jpeg', None))
    eq(Win32MimeTypesTestCase.db.guess_type('image.png'), ('image/png', None))

Win32MimeTypesTestCase = test_mimetypes.Win32MimeTypesTestCase()
Win32MimeTypesTestCase.setUp()
test_registry_parsing()
