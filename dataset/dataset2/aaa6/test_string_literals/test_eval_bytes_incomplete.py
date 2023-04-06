import os
import sys
import shutil
import tempfile
import unittest
import warnings
import test_string_literals

def test_eval_bytes_incomplete():
    TestLiterals.assertRaises(SyntaxError, eval, " b'\\x' ")
    TestLiterals.assertRaises(SyntaxError, eval, " b'\\x0' ")

TestLiterals = test_string_literals.TestLiterals()
test_eval_bytes_incomplete()
