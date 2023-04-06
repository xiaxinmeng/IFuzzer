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

def test_parse_in_error():
    try:
        1 / 0
    except Exception:
        with ASTHelpers_Test.assertRaises(SyntaxError) as e:
            ast.literal_eval("'\\U'")
        ASTHelpers_Test.assertIsNotNone(e.exception.__context__)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_parse_in_error()
