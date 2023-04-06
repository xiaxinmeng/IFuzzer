import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_missing_expression():
    TestCase.assertAllRaise(SyntaxError, 'f-string: empty expression not allowed', ["f'{}'", "f'{ }'f' {} '", "f'{!r}'", "f'{ !r}'", "f'{10:{ }}'", "f' { } '", "f'''{\t\x0c\r\n}'''", "f'{!x}'", "f'{ !xr}'", "f'{!x:}'", "f'{!x:a}'", "f'{ !xr:}'", "f'{ !xr:a}'", "f'{!}'", "f'{:}'", "f'{!'", "f'{!s:'", "f'{:'", "f'{:x'"])
    TestCase.assertAllRaise(SyntaxError, 'invalid non-printable character U\\+00A0', ["f'''{\xa0}'''", '\xa0'])

TestCase = test_fstring.TestCase()
test_missing_expression()
