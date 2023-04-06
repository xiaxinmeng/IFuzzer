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

def test__all__():
    support.check__all__(MiscTestCase, mimetypes)

MiscTestCase = test_mimetypes.MiscTestCase()
test__all__()
