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

def test_call():
    s = 'func(x, y=2, **kw)'
    call = ASTValidatorTests._parse_value(s)
    ASTValidatorTests._check_content(s, call.func, 'func')
    ASTValidatorTests._check_content(s, call.keywords[0].value, '2')
    ASTValidatorTests._check_content(s, call.keywords[1].value, 'kw')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_call()
