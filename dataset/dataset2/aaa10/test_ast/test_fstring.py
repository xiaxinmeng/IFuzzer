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

def test_fstring():
    s = 'x = f"abc {x + y} abc"'
    fstr = EndPositionTests._parse_value(s)
    binop = fstr.values[1].value
    EndPositionTests._check_content(s, binop, 'x + y')

EndPositionTests = test_ast.EndPositionTests()
test_fstring()
