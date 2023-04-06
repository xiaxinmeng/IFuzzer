from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_param_no_docstring():
    function = ClinicParserTest.parse_function("\nmodule os\nos.access\n    follow_symlinks: bool = True\n    something_else: str = ''")
    p = function.parameters['follow_symlinks']
    ClinicParserTest.assertEqual(3, len(function.parameters))
    ClinicParserTest.assertIsInstance(function.parameters['something_else'].converter, clinic.str_converter)

ClinicParserTest = test_clinic.ClinicParserTest()
test_param_no_docstring()
