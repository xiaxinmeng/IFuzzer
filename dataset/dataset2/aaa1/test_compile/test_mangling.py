import dis
import math
import os
import unittest
import sys
import _ast
import tempfile
import types
from test import support
from test.support import script_helper
from test.support.os_helper import FakePath
import builtins

import dis, io
import test_compile

def test_mangling():

    class A:

        def f():
            __mangled = 1
            __not_mangled__ = 2
            import __mangled_mod
            import __package__.module
    TestSpecifics.assertIn('_A__mangled', A.f.__code__.co_varnames)
    TestSpecifics.assertIn('__not_mangled__', A.f.__code__.co_varnames)
    TestSpecifics.assertIn('_A__mangled_mod', A.f.__code__.co_varnames)
    TestSpecifics.assertIn('__package__', A.f.__code__.co_varnames)

TestSpecifics = test_compile.TestSpecifics()
test_mangling()
