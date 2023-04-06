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

@support.cpython_only
def test_issue31592():
    import unicodedata

    def bad_normalize(*args):
        return None
    with support.swap_attr(unicodedata, 'normalize', bad_normalize):
        AST_Tests.assertRaises(TypeError, ast.parse, 'ϕ')

AST_Tests = test_ast.AST_Tests()
test_issue31592()
