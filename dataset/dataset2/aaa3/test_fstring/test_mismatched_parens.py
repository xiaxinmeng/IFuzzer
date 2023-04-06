import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_mismatched_parens():
    TestCase.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\}' does not match opening parenthesis '\\('", ["f'{((}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\)' does not match opening parenthesis '\\['", ["f'{a[4)}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\]' does not match opening parenthesis '\\('", ["f'{a(4]}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\}' does not match opening parenthesis '\\['", ["f'{a[4}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: closing parenthesis '\\}' does not match opening parenthesis '\\('", ["f'{a(4}'"])
    TestCase.assertRaises(SyntaxError, eval, "f'{" + '(' * 500 + "}'")

TestCase = test_fstring.TestCase()
test_mismatched_parens()
