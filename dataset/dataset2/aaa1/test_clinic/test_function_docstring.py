from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_function_docstring():
    function = ClinicParserTest.parse_function('\nmodule os\nos.stat as os_stat_fn\n\n   path: str\n       Path to be examined\n\nPerform a stat system call on the given path.')
    ClinicParserTest.assertEqual('\nstat($module, /, path)\n--\n\nPerform a stat system call on the given path.\n\n  path\n    Path to be examined\n'.strip(), function.docstring)

ClinicParserTest = test_clinic.ClinicParserTest()
test_function_docstring()
