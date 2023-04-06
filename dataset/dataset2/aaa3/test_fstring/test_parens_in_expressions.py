import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_parens_in_expressions():
    TestCase.assertEqual(f'{(3,)}', '(3,)')
    TestCase.assertAllRaise(SyntaxError, 'f-string: invalid syntax', ["f'{,}'", "f'{,}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: unmatched '\\)'", ["f'{3)+(4}'"])
    TestCase.assertAllRaise(SyntaxError, 'EOL while scanning string literal', ["f'{\n}'"])

TestCase = test_fstring.TestCase()
test_parens_in_expressions()
