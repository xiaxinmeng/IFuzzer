import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_walrus():
    x = 20
    TestCase.assertEqual(f'{x:=10}', '        20')
    TestCase.assertEqual(f'{(x := 10)}', '10')
    TestCase.assertEqual(x, 10)

TestCase = test_fstring.TestCase()
test_walrus()
