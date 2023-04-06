from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_function_not_at_column_0():
    function = ClinicParserTest.parse_function('\n  module foo\n  foo.bar\n    x: int\n      Nested docstring here, goeth.\n    *\n    y: str\n  Not at column 0!\n')
    ClinicParserTest.assertEqual('\nbar($module, /, x, *, y)\n--\n\nNot at column 0!\n\n  x\n    Nested docstring here, goeth.\n'.strip(), function.docstring)

ClinicParserTest = test_clinic.ClinicParserTest()
test_function_not_at_column_0()
