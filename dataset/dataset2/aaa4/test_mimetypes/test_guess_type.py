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

def test_guess_type():
    eq = MimetypesCliTestCase.assertEqual
    type_info = MimetypesCliTestCase.mimetypes_cmd('-l', 'foo.pic')
    eq(type_info, 'type: image/pict encoding: None')
    type_info = MimetypesCliTestCase.mimetypes_cmd('foo.pic')
    eq(type_info, "I don't know anything about type foo.pic")

MimetypesCliTestCase = test_mimetypes.MimetypesCliTestCase()

test_guess_type()
