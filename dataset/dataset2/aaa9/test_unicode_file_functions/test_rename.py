import os
import sys
import unittest
import warnings
from unicodedata import normalize
from test import support
from test.support import os_helper
import test_unicode_file_functions

def test_rename():
    for name in UnicodeFileTests.files:
        os.rename(name, 'tmp')
        os.rename('tmp', name)

UnicodeFileTests = test_unicode_file_functions.UnicodeFileTests()
test_rename()
