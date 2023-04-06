import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_file_utf8():
    TestLiterals.check_encoding('utf-8')

TestLiterals = test_string_literals.TestLiterals()
TestLiterals.setUp()
test_file_utf8()
