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

def test_guess_extension():
    eq = MimetypesCliTestCase.assertEqual
    extension = MimetypesCliTestCase.mimetypes_cmd('-l', '-e', 'image/jpg')
    eq(extension, '.jpg')
    extension = MimetypesCliTestCase.mimetypes_cmd('-e', 'image/jpg')
    eq(extension, "I don't know anything about type image/jpg")
    extension = MimetypesCliTestCase.mimetypes_cmd('-e', 'image/jpeg')
    eq(extension, '.jpg')

MimetypesCliTestCase = test_mimetypes.MimetypesCliTestCase()

test_guess_extension()
