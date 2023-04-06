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

def test_import_from_multi_line():
    s = dedent('\n            from x.y.z import (\n                a, b, c as c\n            )\n        ').strip()
    imp = ast.parse(s).body[0]
    EndPositionTests._check_end_pos(imp, 3, 1)

EndPositionTests = test_ast.EndPositionTests()
test_import_from_multi_line()
