import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_yield():

    def fn(y):
        f'y:{(yield (y * 2))}'
        f'{(yield)}'
    g = fn(4)
    TestCase.assertEqual(next(g), 8)
    TestCase.assertEqual(next(g), None)

TestCase = test_fstring.TestCase()
test_yield()
