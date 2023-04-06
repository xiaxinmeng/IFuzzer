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

def test_literal_eval_trailing_ws():
    ASTHelpers_Test.assertEqual(ast.literal_eval('    -1'), -1)
    ASTHelpers_Test.assertEqual(ast.literal_eval('\t\t-1'), -1)
    ASTHelpers_Test.assertEqual(ast.literal_eval(' \t -1'), -1)
    ASTHelpers_Test.assertRaises(IndentationError, ast.literal_eval, '\n -1')

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_literal_eval_trailing_ws()
