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

def test_set():
    ASTValidatorTests.expr(ast.Set([None]), 'None disallowed')
    s = ast.Set([ast.Name('x', ast.Store())])
    ASTValidatorTests.expr(s, 'must have Load context')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_set()
