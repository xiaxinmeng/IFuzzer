import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_invalid_syntax_error_message():
    with TestCase.assertRaisesRegex(SyntaxError, 'f-string: invalid syntax'):
        compile("f'{a $ b}'", '?', 'exec')

TestCase = test_fstring.TestCase()
test_invalid_syntax_error_message()
