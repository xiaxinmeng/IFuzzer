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

def test_preferred_extension():

    def check_extensions():
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/octet-stream'), '.bin')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/postscript'), '.ps')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/vnd.apple.mpegurl'), '.m3u')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/vnd.ms-excel'), '.xls')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/vnd.ms-powerpoint'), '.ppt')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/x-texinfo'), '.texi')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/x-troff'), '.roff')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('application/xml'), '.xsl')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('audio/mpeg'), '.mp3')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('image/jpeg'), '.jpg')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('image/tiff'), '.tiff')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('message/rfc822'), '.eml')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('text/html'), '.html')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('text/plain'), '.txt')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('video/mpeg'), '.mpeg')
        MimeTypesTestCase.assertEqual(mimetypes.guess_extension('video/quicktime'), '.mov')
    check_extensions()
    mimetypes.init()
    check_extensions()

MimeTypesTestCase = test_mimetypes.MimeTypesTestCase()
test_preferred_extension()
