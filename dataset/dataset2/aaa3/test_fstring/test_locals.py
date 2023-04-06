import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_locals():
    value = 123
    TestCase.assertEqual(f'v:{value}', 'v:123')

TestCase = test_fstring.TestCase()
test_locals()
