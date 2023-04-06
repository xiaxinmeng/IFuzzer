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

def test_iter_fields():
    node = ast.parse('foo()', mode='eval')
    d = dict(ast.iter_fields(node.body))
    ASTHelpers_Test.assertEqual(d.pop('func').id, 'foo')
    ASTHelpers_Test.assertEqual(d, {'keywords': [], 'args': []})

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_iter_fields()
