from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_explicit_parameters_in_docstring():
    function = ClinicParserTest.parse_function("\nmodule foo\nfoo.bar\n  x: int\n     Documentation for x.\n  y: int\n\nThis is the documentation for foo.\n\nOkay, we're done here.\n")
    ClinicParserTest.assertEqual("\nbar($module, /, x, y)\n--\n\nThis is the documentation for foo.\n\n  x\n    Documentation for x.\n\nOkay, we're done here.\n".strip(), function.docstring)

ClinicParserTest = test_clinic.ClinicParserTest()
test_explicit_parameters_in_docstring()
