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

def test_ast_validation():
    snippets_to_validate = test_ast.exec_tests + test_ast.single_tests + test_ast.eval_tests
    for snippet in snippets_to_validate:
        tree = ast.parse(snippet)
        compile(tree, '<string>', 'exec')

AST_Tests = test_ast.AST_Tests()
test_ast_validation()
