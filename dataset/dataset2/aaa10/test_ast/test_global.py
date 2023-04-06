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

def test_global():
    ASTValidatorTests.stmt(ast.Global([]), 'empty names on Global')

ASTValidatorTests = test_ast.ASTValidatorTests()
test_global()
