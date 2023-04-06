import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_ast():

    class X:

        def __init__(TestCase):
            TestCase.called = False

        def __call__(TestCase):
            TestCase.called = True
            return 4
    x = X()
    expr = "\na = 10\nf'{a * x()}'"
    t = ast.parse(expr)
    c = compile(t, '', 'exec')
    TestCase.assertFalse(x.called)
    exec(c)
    TestCase.assertTrue(x.called)

TestCase = test_fstring.TestCase()
test_ast()
