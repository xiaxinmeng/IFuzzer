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

def test_module():
    m = ast.Interactive([ast.Expr(ast.Name('x', ast.Store()))])
    AST_Tests.mod(m, 'must have Load context', 'single')
    m = ast.Expression(ast.Name('x', ast.Store()))
    AST_Tests.mod(m, 'must have Load context', 'eval')

AST_Tests = test_ast.AST_Tests()
test_module()
