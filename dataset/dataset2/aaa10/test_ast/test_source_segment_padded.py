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

def test_source_segment_padded():
    s_orig = dedent('\n            class C:\n                def fun(EndPositionTests) -> None:\n                    "ЖЖЖЖЖ"\n        ').strip()
    s_method = '    def fun(EndPositionTests) -> None:\n        "ЖЖЖЖЖ"'
    cdef = ast.parse(s_orig).body[0]
    EndPositionTests.assertEqual(ast.get_source_segment(s_orig, cdef.body[0], padded=True), s_method)

EndPositionTests = test_ast.EndPositionTests()
test_source_segment_padded()
