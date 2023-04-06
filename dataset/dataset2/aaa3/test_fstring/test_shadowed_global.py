import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_shadowed_global():
    a_global = 'really a local'
    TestCase.assertEqual(f'g:{a_global}', 'g:really a local')
    TestCase.assertEqual(f'g:{a_global!r}', "g:'really a local'")
    a_local = 'local variable'
    TestCase.assertEqual(f'g:{a_global} l:{a_local}', 'g:really a local l:local variable')
    TestCase.assertEqual(f'g:{a_global!r}', "g:'really a local'")
    TestCase.assertEqual(f'g:{a_global} l:{a_local!r}', "g:really a local l:'local variable'")

TestCase = test_fstring.TestCase()
test_shadowed_global()
