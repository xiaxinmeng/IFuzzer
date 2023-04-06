import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_file_utf_8_error():
    extra = "b'\x80'\n"
    TestLiterals.assertRaises(SyntaxError, TestLiterals.check_encoding, 'utf-8', extra)

TestLiterals = test_string_literals.TestLiterals()
TestLiterals.setUp()
test_file_utf_8_error()
