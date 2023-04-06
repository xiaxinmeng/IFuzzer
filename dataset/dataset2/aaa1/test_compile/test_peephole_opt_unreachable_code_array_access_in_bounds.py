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

@support.cpython_only
def test_peephole_opt_unreachable_code_array_access_in_bounds():
    """Regression test for issue35193 when run under clang msan."""

    def unused_code_at_end():
        return 3
        raise RuntimeError('unreachable')
    TestSpecifics.assertEqual('RETURN_VALUE', list(dis.get_instructions(unused_code_at_end))[-1].opname)

TestSpecifics = test_compile.TestSpecifics()
test_peephole_opt_unreachable_code_array_access_in_bounds()
