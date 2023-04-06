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

def test_non_interned_future_from_ast():
    mod = ast.parse('from __future__ import division')
    AST_Tests.assertIsInstance(mod.body[0], ast.ImportFrom)
    mod.body[0].module = ' __future__ '.strip()
    compile(mod, '<test>', 'exec')

AST_Tests = test_ast.AST_Tests()
test_non_interned_future_from_ast()
