import os
import sys
import unittest
import warnings
from unicodedata import normalize
from test import support
from test.support import os_helper
import test_unicode_file_functions

def test_directory():
    dirname = os.path.join(os_helper.TESTFN, 'Grüß-曨曩曫')
    filename = 'ß-曨曩曫'
    with os_helper.temp_cwd(dirname):
        with open(filename, 'wb') as f:
            f.write((filename + '\n').encode('utf-8'))
        os.access(filename, os.R_OK)
        os.remove(filename)

UnicodeFileTests = test_unicode_file_functions.UnicodeFileTests()
test_directory()
