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

def test_literal_eval_complex():
    ASTHelpers_Test.assertEqual(ast.literal_eval('6j'), 6j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('-6j'), -6j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('6.75j'), 6.75j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('-6.75j'), -6.75j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('3+6j'), 3 + 6j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('-3+6j'), -3 + 6j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('3-6j'), 3 - 6j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('-3-6j'), -3 - 6j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('3.25+6.75j'), 3.25 + 6.75j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('-3.25+6.75j'), -3.25 + 6.75j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('3.25-6.75j'), 3.25 - 6.75j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('-3.25-6.75j'), -3.25 - 6.75j)
    ASTHelpers_Test.assertEqual(ast.literal_eval('(3+6j)'), 3 + 6j)
    ASTHelpers_Test.assertRaises(ValueError, ast.literal_eval, '-6j+3')
    ASTHelpers_Test.assertRaises(ValueError, ast.literal_eval, '-6j+3j')
    ASTHelpers_Test.assertRaises(ValueError, ast.literal_eval, '3+-6j')
    ASTHelpers_Test.assertRaises(ValueError, ast.literal_eval, '3+(0+6j)')
    ASTHelpers_Test.assertRaises(ValueError, ast.literal_eval, '-(3+6j)')

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_literal_eval_complex()
