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

def test_func_def():
    s = dedent('\n            def func(x: int,\n                     *args: str,\n                     z: float = 0,\n                     **kwargs: Any) -> bool:\n                return True\n            ').strip()
    fdef = ast.parse(s).body[0]
    EndPositionTests._check_end_pos(fdef, 5, 15)
    EndPositionTests._check_content(s, fdef.body[0], 'return True')
    EndPositionTests._check_content(s, fdef.args.args[0], 'x: int')
    EndPositionTests._check_content(s, fdef.args.args[0].annotation, 'int')
    EndPositionTests._check_content(s, fdef.args.kwarg, 'kwargs: Any')
    EndPositionTests._check_content(s, fdef.args.kwarg.annotation, 'Any')

EndPositionTests = test_ast.EndPositionTests()
test_func_def()
