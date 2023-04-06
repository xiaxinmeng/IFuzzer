import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_file_iso_8859_1():
    TestLiterals.check_encoding('iso-8859-1')

TestLiterals = test_string_literals.TestLiterals()
TestLiterals.setUp()
test_file_iso_8859_1()
