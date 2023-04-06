import sys
import unittest
import warnings
from test import support
from test.support import warnings_helper
from codeop import compile_command, PyCF_DONT_IMPLY_DEDENT
import io
import test_codeop

def test_warning():
    with warnings_helper.check_warnings(('.*literal', SyntaxWarning), ('.*invalid', DeprecationWarning)) as w:
        compile_command("'\\e' is 0")
        CodeopTests.assertEqual(len(w.warnings), 2)
    with warnings.catch_warnings(), CodeopTests.assertRaises(SyntaxError):
        warnings.simplefilter('error', SyntaxWarning)
        compile_command('1 is 1', symbol='exec')

CodeopTests = test_codeop.CodeopTests()
test_warning()
