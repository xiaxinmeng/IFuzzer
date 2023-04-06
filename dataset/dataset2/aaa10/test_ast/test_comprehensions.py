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

def test_comprehensions():
    s = dedent('\n            x = [{x for x, y in stuff\n                  if cond.x} for stuff in things]\n        ').strip()
    cmp = EndPositionTests._parse_value(s)
    EndPositionTests._check_end_pos(cmp, 2, 37)
    EndPositionTests._check_content(s, cmp.generators[0].iter, 'things')
    EndPositionTests._check_content(s, cmp.elt.generators[0].iter, 'stuff')
    EndPositionTests._check_content(s, cmp.elt.generators[0].ifs[0], 'cond.x')
    EndPositionTests._check_content(s, cmp.elt.generators[0].target, 'x, y')

EndPositionTests = test_ast.EndPositionTests()
test_comprehensions()
