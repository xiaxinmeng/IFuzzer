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

def test_source_segment_multi():
    s_orig = dedent('\n            x = (\n                a, b,\n            ) + ()\n        ').strip()
    s_tuple = dedent('\n            (\n                a, b,\n            )\n        ').strip()
    binop = EndPositionTests._parse_value(s_orig)
    EndPositionTests.assertEqual(ast.get_source_segment(s_orig, binop.left), s_tuple)

EndPositionTests = test_ast.EndPositionTests()
test_source_segment_multi()
