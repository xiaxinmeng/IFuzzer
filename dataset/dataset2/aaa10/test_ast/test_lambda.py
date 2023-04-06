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

def test_lambda():
    s = 'lambda x, *y: None'
    lam = ASTValidatorTests._parse_value(s)
    ASTValidatorTests._check_content(s, lam.body, 'None')
    ASTValidatorTests._check_content(s, lam.args.args[0], 'x')
    ASTValidatorTests._check_content(s, lam.args.vararg, 'y')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_lambda()
