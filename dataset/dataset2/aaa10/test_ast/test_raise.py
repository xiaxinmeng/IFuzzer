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

def test_raise():
    r = ast.Raise(None, ast.Num(3))
    ASTValidatorTests.stmt(r, 'Raise with cause but no exception')
    r = ast.Raise(ast.Name('x', ast.Store()), None)
    ASTValidatorTests.stmt(r, 'must have Load context')
    r = ast.Raise(ast.Num(4), ast.Name('x', ast.Store()))
    ASTValidatorTests.stmt(r, 'must have Load context')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_raise()
