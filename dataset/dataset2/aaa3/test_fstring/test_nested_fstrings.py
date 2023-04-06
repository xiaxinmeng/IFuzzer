import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_nested_fstrings():
    y = 5
    TestCase.assertEqual(f"{f'{0}' * 3}", '000')
    TestCase.assertEqual(f"{f'{y}' * 3}", '555')

TestCase = test_fstring.TestCase()
test_nested_fstrings()
