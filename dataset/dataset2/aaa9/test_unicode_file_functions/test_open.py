import os
import sys
import unittest
import warnings
from unicodedata import normalize
from test import support
from test.support import os_helper
import test_unicode_file_functions

def test_open():
    for name in UnicodeFileTests.files:
        f = open(name, 'wb')
        f.write((name + '\n').encode('utf-8'))
        f.close()
        os.stat(name)
        UnicodeFileTests._apply_failure(os.listdir, name, UnicodeFileTests._listdir_failure)

UnicodeFileTests = test_unicode_file_functions.UnicodeFileTests()
test_open()
