import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_concat_empty(x, expected):
    flag = 0
    if f'{x}':
        flag = 1
    else:
        flag = 2
    TestCase.assertEqual(flag, expected)

TestCase = test_fstring.TestCase()
test_concat_empty()
