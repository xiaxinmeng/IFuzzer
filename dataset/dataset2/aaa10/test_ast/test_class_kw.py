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

def test_class_kw():
    s = 'class S(metaclass=abc.ABCMeta): pass'
    cdef = ast.parse(s).body[0]
    EndPositionTests._check_content(s, cdef.keywords[0].value, 'abc.ABCMeta')

EndPositionTests = test_ast.EndPositionTests()
test_class_kw()
