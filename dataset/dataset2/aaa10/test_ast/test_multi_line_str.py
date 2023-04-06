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

def test_multi_line_str():
    s = dedent('\n            x = """Some multi-line text.\n\n            It goes on starting from same indent."""\n        ').strip()
    assign = ast.parse(s).body[0]
    EndPositionTests._check_end_pos(assign, 3, 40)
    EndPositionTests._check_end_pos(assign.value, 3, 40)

EndPositionTests = test_ast.EndPositionTests()
test_multi_line_str()
