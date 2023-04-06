import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_yield_send():

    def fn(x):
        yield f'x:{(yield (lambda i: x * i))}'
    g = fn(10)
    the_lambda = next(g)
    TestCase.assertEqual(the_lambda(4), 40)
    TestCase.assertEqual(g.send('string'), 'x:string')

TestCase = test_fstring.TestCase()
test_yield_send()
