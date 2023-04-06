import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_literal_eval():
    with TestCase.assertRaisesRegex(ValueError, 'malformed node or string'):
        ast.literal_eval("f'x'")

TestCase = test_fstring.TestCase()
test_literal_eval()
