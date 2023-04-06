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

def test_continued_str():
    s = dedent('\n            x = "first part" \\\n            "second part"\n        ').strip()
    assign = ast.parse(s).body[0]
    EndPositionTests._check_end_pos(assign, 2, 13)
    EndPositionTests._check_end_pos(assign.value, 2, 13)

EndPositionTests = test_ast.EndPositionTests()
test_continued_str()
