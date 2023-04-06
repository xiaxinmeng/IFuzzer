from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_param_default_expression():
    function = ClinicParserTest.parse_function("module os\nos.access\n    follow_symlinks: int(c_default='MAXSIZE') = sys.maxsize")
    p = function.parameters['follow_symlinks']
    ClinicParserTest.assertEqual(sys.maxsize, p.default)
    ClinicParserTest.assertEqual('MAXSIZE', p.converter.c_default)
    s = ClinicParserTest.parse_function_should_fail('module os\nos.access\n    follow_symlinks: int = sys.maxsize')
    ClinicParserTest.assertEqual(s, "Error on line 0:\nWhen you specify a named constant ('sys.maxsize') as your default value,\nyou MUST specify a valid c_default.\n")

ClinicParserTest = test_clinic.ClinicParserTest()
test_param_default_expression()
