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

def test_augassign():
    aug = ast.AugAssign(ast.Name('x', ast.Load()), ast.Add(), ast.Name('y', ast.Load()))
    ASTValidatorTests.stmt(aug, 'must have Store context')
    aug = ast.AugAssign(ast.Name('x', ast.Store()), ast.Add(), ast.Name('y', ast.Store()))
    ASTValidatorTests.stmt(aug, 'must have Load context')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_augassign()
