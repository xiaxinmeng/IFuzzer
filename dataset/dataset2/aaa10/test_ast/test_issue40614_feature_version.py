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

def test_issue40614_feature_version():
    ast.parse('f"{x=}"', feature_version=(3, 8))
    with AST_Tests.assertRaises(SyntaxError):
        ast.parse('f"{x=}"', feature_version=(3, 7))

AST_Tests = test_ast.AST_Tests()
test_issue40614_feature_version()
