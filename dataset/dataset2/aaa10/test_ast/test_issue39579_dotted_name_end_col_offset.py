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

def test_issue39579_dotted_name_end_col_offset():
    tree = ast.parse('@a.b.c\ndef f(): pass')
    attr_b = tree.body[0].decorator_list[0].value
    AST_Tests.assertEqual(attr_b.end_col_offset, 4)

AST_Tests = test_ast.AST_Tests()
test_issue39579_dotted_name_end_col_offset()
