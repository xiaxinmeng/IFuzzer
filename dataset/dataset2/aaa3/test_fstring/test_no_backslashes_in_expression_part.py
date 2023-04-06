import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_no_backslashes_in_expression_part():
    TestCase.assertAllRaise(SyntaxError, 'f-string expression part cannot include a backslash', ["f'{\\'a\\'}'", "f'{\\t3}'", "f'{\\}'", "rf'{\\'a\\'}'", "rf'{\\t3}'", "rf'{\\}'", 'rf\'{"\\N{LEFT CURLY BRACKET}"}\'', "f'{\\n}'"])

TestCase = test_fstring.TestCase()
test_no_backslashes_in_expression_part()
