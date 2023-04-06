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

def test_elif_stmt_start_position_with_else():
    node = ast.parse('if a:\n    pass\nelif b:\n    pass\nelse:\n    pass\n')
    elif_stmt = node.body[0].orelse[0]
    ASTHelpers_Test.assertEqual(elif_stmt.lineno, 3)
    ASTHelpers_Test.assertEqual(elif_stmt.col_offset, 0)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_elif_stmt_start_position_with_else()
