import re
import unittest
from test import support
from test import test_syntax
import test_syntax

@support.cpython_only
def test_nested_named_except_blocks():
    code = ''
    for i in range(12):
        code += f"{'    ' * i}try:\n"
        code += f"{'    ' * (i + 1)}raise Exception\n"
        code += f"{'    ' * i}except Exception as e:\n"
    code += f"{' ' * 4 * 12}pass"
    SyntaxTestCase._check_error(code, 'too many statically nested blocks')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_nested_named_except_blocks()
