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

def test_attribute_spaces():
    s = 'func(x. y .z)'
    call = EndPositionTests._parse_value(s)
    EndPositionTests._check_content(s, call, s)
    EndPositionTests._check_content(s, call.args[0], 'x. y .z')

EndPositionTests = test_ast.EndPositionTests()
test_attribute_spaces()
