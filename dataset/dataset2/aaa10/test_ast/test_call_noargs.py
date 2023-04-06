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

def test_call_noargs():
    s = 'x[0]()'
    call = EndPositionTests._parse_value(s)
    EndPositionTests._check_content(s, call.func, 'x[0]')
    EndPositionTests._check_end_pos(call, 1, 6)

EndPositionTests = test_ast.EndPositionTests()
test_call_noargs()
