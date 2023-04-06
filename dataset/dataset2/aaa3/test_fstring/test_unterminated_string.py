import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_unterminated_string():
    TestCase.assertAllRaise(SyntaxError, 'f-string: unterminated string', ['f\'{"x\'', 'f\'{"x}\'', 'f\'{("x\'', 'f\'{("x}\''])

TestCase = test_fstring.TestCase()
test_unterminated_string()
