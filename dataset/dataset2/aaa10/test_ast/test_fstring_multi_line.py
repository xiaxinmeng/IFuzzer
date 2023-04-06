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

def test_fstring_multi_line():
    s = dedent('\n            f"""Some multi-line text.\n            {\n            arg_one\n            +\n            arg_two\n            }\n            It goes on..."""\n        ').strip()
    fstr = EndPositionTests._parse_value(s)
    binop = fstr.values[1].value
    EndPositionTests._check_end_pos(binop, 5, 7)
    EndPositionTests._check_content(s, binop.left, 'arg_one')
    EndPositionTests._check_content(s, binop.right, 'arg_two')

EndPositionTests = test_ast.EndPositionTests()
test_fstring_multi_line()
