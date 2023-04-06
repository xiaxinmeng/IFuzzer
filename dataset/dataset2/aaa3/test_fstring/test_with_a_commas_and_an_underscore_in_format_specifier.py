import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_with_a_commas_and_an_underscore_in_format_specifier():
    error_msg = re.escape("Cannot specify both ',' and '_'.")
    with TestCase.assertRaisesRegex(ValueError, error_msg):
        f'{1:,_}'

TestCase = test_fstring.TestCase()
test_with_a_commas_and_an_underscore_in_format_specifier()
