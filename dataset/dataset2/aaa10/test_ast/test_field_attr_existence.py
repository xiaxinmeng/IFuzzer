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

def test_field_attr_existence():
    for (name, item) in ast.__dict__.items():
        if AST_Tests._is_ast_node(name, item):
            if name == 'Index':
                continue
            x = item()
            if isinstance(x, ast.AST):
                AST_Tests.assertEqual(type(x._fields), tuple)

AST_Tests = test_ast.AST_Tests()
test_field_attr_existence()
