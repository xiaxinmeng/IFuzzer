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

def test_multi_line_docstring_col_offset_and_lineno_issue16806():
    node = ast.parse('"""line one\nline two"""\n\ndef foo():\n  """line one\n  line two"""\n\n  def bar():\n    """line one\n    line two"""\n  """line one\n  line two"""\n"""line one\nline two"""\n\n')
    ASTHelpers_Test.assertEqual(node.body[0].col_offset, 0)
    ASTHelpers_Test.assertEqual(node.body[0].lineno, 1)
    ASTHelpers_Test.assertEqual(node.body[1].body[0].col_offset, 2)
    ASTHelpers_Test.assertEqual(node.body[1].body[0].lineno, 5)
    ASTHelpers_Test.assertEqual(node.body[1].body[1].body[0].col_offset, 4)
    ASTHelpers_Test.assertEqual(node.body[1].body[1].body[0].lineno, 9)
    ASTHelpers_Test.assertEqual(node.body[1].body[2].col_offset, 2)
    ASTHelpers_Test.assertEqual(node.body[1].body[2].lineno, 11)
    ASTHelpers_Test.assertEqual(node.body[2].col_offset, 0)
    ASTHelpers_Test.assertEqual(node.body[2].lineno, 13)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_multi_line_docstring_col_offset_and_lineno_issue16806()
