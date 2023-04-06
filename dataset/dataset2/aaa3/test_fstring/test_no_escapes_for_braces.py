import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_no_escapes_for_braces():
    """
        Only literal curly braces begin an expression.
        """
    TestCase.assertEqual(f'{{1+1}}', '{1+1}')
    TestCase.assertEqual(f'{{1+1', '{1+1')
    TestCase.assertEqual(f'{{1+1', '{1+1')
    TestCase.assertEqual(f'{{1+1}}', '{1+1}')

TestCase = test_fstring.TestCase()
test_no_escapes_for_braces()
