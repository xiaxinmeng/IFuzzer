from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_param_default_parameters_out_of_order():
    s = ClinicParserTest.parse_function_should_fail('\nmodule os\nos.access\n    follow_symlinks: bool = True\n    something_else: str')
    ClinicParserTest.assertEqual(s, "Error on line 0:\nCan't have a parameter without a default ('something_else')\nafter a parameter with a default!\n")

ClinicParserTest = test_clinic.ClinicParserTest()
test_param_default_parameters_out_of_order()
