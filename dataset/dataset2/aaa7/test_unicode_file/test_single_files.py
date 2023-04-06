import os, glob, time, shutil
import sys
import unicodedata
import unittest
from test.support import run_unittest
from test.support.os_helper import rmtree, change_cwd, TESTFN_UNICODE, TESTFN_UNENCODABLE, create_empty_file
import test_unicode_file

def test_single_files():
    TestUnicodeFiles._test_single(TESTFN_UNICODE)
    if TESTFN_UNENCODABLE is not None:
        TestUnicodeFiles._test_single(TESTFN_UNENCODABLE)

TestUnicodeFiles = test_unicode_file.TestUnicodeFiles()
test_single_files()
