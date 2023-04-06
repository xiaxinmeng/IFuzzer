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

def test_while():
    ASTValidatorTests.stmt(ast.While(ast.Num(3), [], []), 'empty body on While')
    ASTValidatorTests.stmt(ast.While(ast.Name('x', ast.Store()), [ast.Pass()], []), 'must have Load context')
    ASTValidatorTests.stmt(ast.While(ast.Num(3), [ast.Pass()], [ast.Expr(ast.Name('x', ast.Store()))]), 'must have Load context')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_while()
