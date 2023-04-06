import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_not_equal():
    TestCase.assertEqual(f'{3 != 4}', 'True')
    TestCase.assertEqual(f'{3 != 4:}', 'True')
    TestCase.assertEqual(f'{3 != 4!s}', 'True')
    TestCase.assertEqual(f'{3 != 4!s:.3}', 'Tru')

TestCase = test_fstring.TestCase()
test_not_equal()
