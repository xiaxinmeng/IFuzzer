import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_file_latin9():
    TestLiterals.check_encoding('latin9')

TestLiterals = test_string_literals.TestLiterals()
TestLiterals.setUp()
test_file_latin9()
