import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_with_two_commas_in_format_specifier():
    error_msg = re.escape("Cannot specify ',' with ','.")
    with TestCase.assertRaisesRegex(ValueError, error_msg):
        f'{1:,,}'

TestCase = test_fstring.TestCase()
test_with_two_commas_in_format_specifier()
