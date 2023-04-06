import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_equal_equal():
    TestCase.assertEqual(f'{0 == 1}', 'False')

TestCase = test_fstring.TestCase()
test_equal_equal()
