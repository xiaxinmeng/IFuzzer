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

def test_binop():
    s = dedent('\n            (1 * 2 + (3 ) +\n                 4\n            )\n        ').strip()
    binop = EndPositionTests._parse_value(s)
    EndPositionTests._check_end_pos(binop, 2, 6)
    EndPositionTests._check_content(s, binop.right, '4')
    EndPositionTests._check_content(s, binop.left, '1 * 2 + (3 )')
    EndPositionTests._check_content(s, binop.left.right, '3')

EndPositionTests = test_ast.EndPositionTests()
test_binop()
