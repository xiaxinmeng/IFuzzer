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

def test_reload_module():
    with support.swap_item(sys.modules, '_ast', None):
        del sys.modules['_ast']
        import _ast as ast1
        del sys.modules['_ast']
        import _ast as ast2
        ModuleStateTests.check_ast_module()
    del ast1
    del ast2
    support.gc_collect()
    ModuleStateTests.check_ast_module()

ModuleStateTests = test_ast.ModuleStateTests()
test_reload_module()
