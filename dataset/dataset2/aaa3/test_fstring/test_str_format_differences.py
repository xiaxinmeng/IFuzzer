import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_str_format_differences():
    d = {'a': 'string', 0: 'integer'}
    a = 0
    TestCase.assertEqual(f'{d[0]}', 'integer')
    TestCase.assertEqual(f"{d['a']}", 'string')
    TestCase.assertEqual(f'{d[a]}', 'integer')
    TestCase.assertEqual('{d[a]}'.format(d=d), 'string')
    TestCase.assertEqual('{d[0]}'.format(d=d), 'integer')

TestCase = test_fstring.TestCase()
test_str_format_differences()
