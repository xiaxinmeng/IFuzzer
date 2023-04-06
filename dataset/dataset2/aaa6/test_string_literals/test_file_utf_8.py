import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_file_utf_8():
    extra = "z = 'ሴ'; assert ord(z) == 0x1234\n"
    TestLiterals.check_encoding('utf-8', extra)

TestLiterals = test_string_literals.TestLiterals()
TestLiterals.setUp()
test_file_utf_8()
