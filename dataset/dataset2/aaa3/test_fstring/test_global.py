import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_global():
    TestCase.assertEqual(f'g:{a_global}', 'g:global variable')
    TestCase.assertEqual(f'g:{a_global!r}', "g:'global variable'")
    a_local = 'local variable'
    TestCase.assertEqual(f'g:{a_global} l:{a_local}', 'g:global variable l:local variable')
    TestCase.assertEqual(f'g:{a_global!r}', "g:'global variable'")
    TestCase.assertEqual(f'g:{a_global} l:{a_local!r}', "g:global variable l:'local variable'")
    TestCase.assertIn("module 'unittest' from", f'{unittest}')

TestCase = test_fstring.TestCase()
test_global()
