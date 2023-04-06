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

def test_dump_incomplete():
    node = ast.Raise(lineno=3, col_offset=4)
    ASTHelpers_Test.assertEqual(ast.dump(node), 'Raise()')
    ASTHelpers_Test.assertEqual(ast.dump(node, include_attributes=True), 'Raise(lineno=3, col_offset=4)')
    node = ast.Raise(exc=ast.Name(id='e', ctx=ast.Load()), lineno=3, col_offset=4)
    ASTHelpers_Test.assertEqual(ast.dump(node), "Raise(exc=Name(id='e', ctx=Load()))")
    ASTHelpers_Test.assertEqual(ast.dump(node, annotate_fields=False), "Raise(Name('e', Load()))")
    ASTHelpers_Test.assertEqual(ast.dump(node, include_attributes=True), "Raise(exc=Name(id='e', ctx=Load()), lineno=3, col_offset=4)")
    ASTHelpers_Test.assertEqual(ast.dump(node, annotate_fields=False, include_attributes=True), "Raise(Name('e', Load()), lineno=3, col_offset=4)")
    node = ast.Raise(cause=ast.Name(id='e', ctx=ast.Load()))
    ASTHelpers_Test.assertEqual(ast.dump(node), "Raise(cause=Name(id='e', ctx=Load()))")
    ASTHelpers_Test.assertEqual(ast.dump(node, annotate_fields=False), "Raise(cause=Name('e', Load()))")

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_dump_incomplete()
