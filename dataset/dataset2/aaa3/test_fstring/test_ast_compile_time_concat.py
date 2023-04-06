import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_ast_compile_time_concat():
    x = ['']
    expr = "x[0] = 'foo' f'{3}'"
    t = ast.parse(expr)
    c = compile(t, '', 'exec')
    exec(c)
    TestCase.assertEqual(x[0], 'foo3')

TestCase = test_fstring.TestCase()
test_ast_compile_time_concat()
