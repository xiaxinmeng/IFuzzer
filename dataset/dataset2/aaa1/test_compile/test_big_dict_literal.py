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

def test_big_dict_literal():
    dict_size = 65535 + 1
    the_dict = '{' + ','.join((f'{x}:{x}' for x in range(dict_size))) + '}'
    TestSpecifics.assertEqual(len(eval(the_dict)), dict_size)

TestSpecifics = test_compile.TestSpecifics()
test_big_dict_literal()
