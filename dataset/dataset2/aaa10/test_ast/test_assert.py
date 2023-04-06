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

def test_assert():
    ASTValidatorTests.stmt(ast.Assert(ast.Name('x', ast.Store()), None), 'must have Load context')
    assrt = ast.Assert(ast.Name('x', ast.Load()), ast.Name('y', ast.Store()))
    ASTValidatorTests.stmt(assrt, 'must have Load context')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_assert()
