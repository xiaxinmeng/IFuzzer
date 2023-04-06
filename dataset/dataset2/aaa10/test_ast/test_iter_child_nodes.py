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

def test_iter_child_nodes():
    node = ast.parse("spam(23, 42, eggs='leek')", mode='eval')
    ASTHelpers_Test.assertEqual(len(list(ast.iter_child_nodes(node.body))), 4)
    iterator = ast.iter_child_nodes(node.body)
    ASTHelpers_Test.assertEqual(next(iterator).id, 'spam')
    ASTHelpers_Test.assertEqual(next(iterator).value, 23)
    ASTHelpers_Test.assertEqual(next(iterator).value, 42)
    ASTHelpers_Test.assertEqual(ast.dump(next(iterator)), "keyword(arg='eggs', value=Constant(value='leek'))")

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_iter_child_nodes()
