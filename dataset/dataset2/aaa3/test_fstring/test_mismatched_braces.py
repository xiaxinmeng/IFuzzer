import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_mismatched_braces():
    TestCase.assertAllRaise(SyntaxError, "f-string: single '}' is not allowed", ["f'{{}'", "f'{{}}}'", "f'}'", "f'x}'", "f'x}x'", "f'\\u007b}'", "f'{3:}>10}'", "f'{3:}}>10}'"])
    TestCase.assertAllRaise(SyntaxError, "f-string: expecting '}'", ["f'{3:{{>10}'", "f'{3'", "f'{3!'", "f'{3:'", "f'{3!s'", "f'{3!s:'", "f'{3!s:3'", "f'x{'", "f'x{x'", "f'{x'", "f'{3:s'", "f'{{{'", "f'{{}}{'", "f'{'"])
    TestCase.assertEqual(f"{'{'}", '{')
    TestCase.assertEqual(f"{'}'}", '}')
    TestCase.assertEqual(f"{3:{'}'}>10}", '}}}}}}}}}3')
    TestCase.assertEqual(f"{2:{'{'}>10}", '{{{{{{{{{2')

TestCase = test_fstring.TestCase()
test_mismatched_braces()
