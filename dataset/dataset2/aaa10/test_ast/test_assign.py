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

def test_assign():
    ASTValidatorTests.stmt(ast.Assign([], ast.Num(3)), 'empty targets on Assign')
    ASTValidatorTests.stmt(ast.Assign([None], ast.Num(3)), 'None disallowed')
    ASTValidatorTests.stmt(ast.Assign([ast.Name('x', ast.Load())], ast.Num(3)), 'must have Store context')
    ASTValidatorTests.stmt(ast.Assign([ast.Name('x', ast.Store())], ast.Name('y', ast.Store())), 'must have Load context')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_assign()
