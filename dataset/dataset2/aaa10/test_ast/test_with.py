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

def test_with():
    p = ast.Pass()
    ASTValidatorTests.stmt(ast.With([], [p]), 'empty items on With')
    i = ast.withitem(ast.Num(3), None)
    ASTValidatorTests.stmt(ast.With([i], []), 'empty body on With')
    i = ast.withitem(ast.Name('x', ast.Store()), None)
    ASTValidatorTests.stmt(ast.With([i], [p]), 'must have Load context')
    i = ast.withitem(ast.Num(3), ast.Name('x', ast.Load()))
    ASTValidatorTests.stmt(ast.With([i], [p]), 'must have Store context')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_with()
