import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_leading_trailing_spaces():
    TestCase.assertEqual(f'{3}', '3')
    TestCase.assertEqual(f'{3}', '3')
    TestCase.assertEqual(f'{3}', '3')
    TestCase.assertEqual(f'{3}', '3')
    TestCase.assertEqual(f'expr={ {x: y for (x, y) in [(1, 2)]}}', 'expr={1: 2}')
    TestCase.assertEqual(f'expr={ {x: y for (x, y) in [(1, 2)]}}', 'expr={1: 2}')

TestCase = test_fstring.TestCase()
test_leading_trailing_spaces()
