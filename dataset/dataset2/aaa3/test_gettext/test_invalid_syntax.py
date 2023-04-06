import os
import base64
import contextlib
import gettext
import unittest
from test import support
from test.support import os_helper
import builtins
import test_gettext

def test_invalid_syntax():
    invalid_expressions = ['x>1', '(n>1', 'n>1)', '42**42**42', '0xa', '1.0', '1e2', 'n>0x1', '+n', '-n', 'n()', 'n(1)', '1+', 'nn', 'n n']
    for expr in invalid_expressions:
        with PluralFormsTestCase.assertRaises(ValueError):
            gettext.c2py(expr)

PluralFormsTestCase = test_gettext.PluralFormsTestCase()
test_invalid_syntax()
