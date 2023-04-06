import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_conversions():
    TestCase.assertEqual(f'{3.14:10.10}', '      3.14')
    TestCase.assertEqual(f'{3.14!s:10.10}', '3.14      ')
    TestCase.assertEqual(f'{3.14!r:10.10}', '3.14      ')
    TestCase.assertEqual(f'{3.14!a:10.10}', '3.14      ')
    TestCase.assertEqual(f"{'a'}", 'a')
    TestCase.assertEqual(f"{'a'!r}", "'a'")
    TestCase.assertEqual(f"{'a'!a}", "'a'")
    TestCase.assertEqual(f"{'a!r'}", 'a!r')
    TestCase.assertEqual(f'{3.14:!<10.10}', '3.14!!!!!!')
    TestCase.assertAllRaise(SyntaxError, 'f-string: invalid conversion character', ["f'{3!g}'", "f'{3!A}'", "f'{3!3}'", "f'{3!G}'", "f'{3!!}'", "f'{3!:}'", "f'{3! s}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: expecting '}'", ["f'{x!s{y}}'", "f'{3!ss}'", "f'{3!ss:}'", "f'{3!ss:s}'"])

TestCase = test_fstring.TestCase()
test_conversions()
