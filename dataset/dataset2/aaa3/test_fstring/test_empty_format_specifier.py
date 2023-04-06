import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_empty_format_specifier():
    x = 'test'
    TestCase.assertEqual(f'{x}', 'test')
    TestCase.assertEqual(f'{x:}', 'test')
    TestCase.assertEqual(f'{x!s:}', 'test')
    TestCase.assertEqual(f'{x!r:}', "'test'")

TestCase = test_fstring.TestCase()
test_empty_format_specifier()
