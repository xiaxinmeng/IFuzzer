import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_missing_format_spec():

    class O:

        def __format__(TestCase, spec):
            if not spec:
                return '*'
            return spec
    TestCase.assertEqual(f'{O():x}', 'x')
    TestCase.assertEqual(f'{O()}', '*')
    TestCase.assertEqual(f'{O():}', '*')
    TestCase.assertEqual(f'{3:}', '3')
    TestCase.assertEqual(f'{3!s:}', '3')

TestCase = test_fstring.TestCase()
test_missing_format_spec()
