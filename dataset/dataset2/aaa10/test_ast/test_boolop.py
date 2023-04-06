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

def test_boolop():
    s = dedent('\n            if (one_condition and\n                    (other_condition or yet_another_one)):\n                pass\n        ').strip()
    bop = ast.parse(s).body[0].test
    ASTValidatorTests._check_end_pos(bop, 2, 44)
    ASTValidatorTests._check_content(s, bop.values[1], 'other_condition or yet_another_one')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_boolop()
