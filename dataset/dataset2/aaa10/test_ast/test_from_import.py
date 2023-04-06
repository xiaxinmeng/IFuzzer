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

def test_from_import():
    im = ast.parse('from . import y').body[0]
    AST_Tests.assertIsNone(im.module)

AST_Tests = test_ast.AST_Tests()
test_from_import()
