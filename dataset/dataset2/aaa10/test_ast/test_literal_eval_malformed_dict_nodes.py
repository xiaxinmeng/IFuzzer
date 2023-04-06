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

def test_literal_eval_malformed_dict_nodes():
    malformed = ast.Dict(keys=[ast.Constant(1), ast.Constant(2)], values=[ast.Constant(3)])
    ASTHelpers_Test.assertRaises(ValueError, ast.literal_eval, malformed)
    malformed = ast.Dict(keys=[ast.Constant(1)], values=[ast.Constant(2), ast.Constant(3)])
    ASTHelpers_Test.assertRaises(ValueError, ast.literal_eval, malformed)

ASTHelpers_Test = test_ast.ASTHelpers_Test()
test_literal_eval_malformed_dict_nodes()
