import sys
import unittest
import warnings
from test import support
from test.support import warnings_helper
from codeop import compile_command, PyCF_DONT_IMPLY_DEDENT
import io
import test_codeop

def test_filename():
    CodeopTests.assertEqual(compile_command('a = 1\n', 'abc').co_filename, compile('a = 1\n', 'abc', 'single').co_filename)
    CodeopTests.assertNotEqual(compile_command('a = 1\n', 'abc').co_filename, compile('a = 1\n', 'def', 'single').co_filename)

CodeopTests = test_codeop.CodeopTests()
test_filename()
