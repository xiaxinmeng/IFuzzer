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

def test_source_segment_tabs():
    s = dedent('\n            class C:\n              \t\x0c  def fun(EndPositionTests) -> None:\n              \t\x0c      pass\n        ').strip()
    s_method = '  \t\x0c  def fun(EndPositionTests) -> None:\n  \t\x0c      pass'
    cdef = ast.parse(s).body[0]
    EndPositionTests.assertEqual(ast.get_source_segment(s, cdef.body[0], padded=True), s_method)

EndPositionTests = test_ast.EndPositionTests()
test_source_segment_tabs()
