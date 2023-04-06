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

def test_importfrom():
    imp = ast.ImportFrom(None, [ast.alias('x', None)], -42)
    ASTValidatorTests.stmt(imp, 'Negative ImportFrom level')
    ASTValidatorTests.stmt(ast.ImportFrom(None, [], 0), 'empty names on ImportFrom')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_importfrom()
