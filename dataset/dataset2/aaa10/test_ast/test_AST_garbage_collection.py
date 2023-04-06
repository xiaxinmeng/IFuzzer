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

def test_AST_garbage_collection():

    class X:
        pass
    a = ast.AST()
    a.x = X()
    a.x.a = a
    ref = weakref.ref(a.x)
    del a
    support.gc_collect()
    AST_Tests.assertIsNone(ref())

AST_Tests = test_ast.AST_Tests()
test_AST_garbage_collection()
