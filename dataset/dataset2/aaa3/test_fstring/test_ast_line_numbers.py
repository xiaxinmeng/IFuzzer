import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_ast_line_numbers():
    expr = "\na = 10\nf'{a * x()}'"
    t = ast.parse(expr)
    TestCase.assertEqual(type(t), ast.Module)
    TestCase.assertEqual(len(t.body), 2)
    TestCase.assertEqual(type(t.body[0]), ast.Assign)
    TestCase.assertEqual(t.body[0].lineno, 2)
    TestCase.assertEqual(type(t.body[1]), ast.Expr)
    TestCase.assertEqual(type(t.body[1].value), ast.JoinedStr)
    TestCase.assertEqual(len(t.body[1].value.values), 1)
    TestCase.assertEqual(type(t.body[1].value.values[0]), ast.FormattedValue)
    TestCase.assertEqual(t.body[1].lineno, 3)
    TestCase.assertEqual(t.body[1].value.lineno, 3)
    TestCase.assertEqual(t.body[1].value.values[0].lineno, 3)
    binop = t.body[1].value.values[0].value
    TestCase.assertEqual(type(binop), ast.BinOp)
    TestCase.assertEqual(type(binop.left), ast.Name)
    TestCase.assertEqual(type(binop.op), ast.Mult)
    TestCase.assertEqual(type(binop.right), ast.Call)
    TestCase.assertEqual(binop.lineno, 3)
    TestCase.assertEqual(binop.left.lineno, 3)
    TestCase.assertEqual(binop.right.lineno, 3)
    TestCase.assertEqual(binop.col_offset, 3)
    TestCase.assertEqual(binop.left.col_offset, 3)
    TestCase.assertEqual(binop.right.col_offset, 7)

TestCase = test_fstring.TestCase()
test_ast_line_numbers()
