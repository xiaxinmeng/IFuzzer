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

def test_yield_await():
    s = dedent('\n            async def f():\n                yield x\n                await y\n        ').strip()
    fdef = ast.parse(s).body[0]
    EndPositionTests._check_content(s, fdef.body[0].value, 'yield x')
    EndPositionTests._check_content(s, fdef.body[1].value, 'await y')

EndPositionTests = test_ast.EndPositionTests()
test_yield_await()
