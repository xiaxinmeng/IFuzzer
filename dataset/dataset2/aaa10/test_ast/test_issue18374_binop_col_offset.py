import ast
import builtins
import dis
import os
import sys
import types
import unittest
import warnings
import weakref
from textwrap import dedent
from test import support
import pickle

import unicodedata
import _ast as ast1
import _ast as ast2
import _ast
import test_ast

def test_issue18374_binop_col_offset():
    tree = ast.parse('4+5+6+7')
    parent_binop = tree.body[0].value
    child_binop = parent_binop.left
    grandchild_binop = child_binop.left
    AST_Tests.assertEqual(parent_binop.col_offset, 0)
    AST_Tests.assertEqual(parent_binop.end_col_offset, 7)
    AST_Tests.assertEqual(child_binop.col_offset, 0)
    AST_Tests.assertEqual(child_binop.end_col_offset, 5)
    AST_Tests.assertEqual(grandchild_binop.col_offset, 0)
    AST_Tests.assertEqual(grandchild_binop.end_col_offset, 3)
    tree = ast.parse('4+5-\\\n 6-7')
    parent_binop = tree.body[0].value
    child_binop = parent_binop.left
    grandchild_binop = child_binop.left
    AST_Tests.assertEqual(parent_binop.col_offset, 0)
    AST_Tests.assertEqual(parent_binop.lineno, 1)
    AST_Tests.assertEqual(parent_binop.end_col_offset, 4)
    AST_Tests.assertEqual(parent_binop.end_lineno, 2)
    AST_Tests.assertEqual(child_binop.col_offset, 0)
    AST_Tests.assertEqual(child_binop.lineno, 1)
    AST_Tests.assertEqual(child_binop.end_col_offset, 2)
    AST_Tests.assertEqual(child_binop.end_lineno, 2)
    AST_Tests.assertEqual(grandchild_binop.col_offset, 0)
    AST_Tests.assertEqual(grandchild_binop.lineno, 1)
    AST_Tests.assertEqual(grandchild_binop.end_col_offset, 3)
    AST_Tests.assertEqual(grandchild_binop.end_lineno, 1)

AST_Tests = test_ast.AST_Tests()
test_issue18374_binop_col_offset()
