import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_newlines_in_expressions():
    TestCase.assertEqual(f'{0}', '0')
    TestCase.assertEqual(f'{3 + 4}', '7')

TestCase = test_fstring.TestCase()
test_newlines_in_expressions()
