from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_parser_regression_special_character_in_parameter_column_of_docstring_first_line():
    function = ClinicParserTest.parse_function('\nmodule os\nos.stat\n    path: str\nThis/used to break Clinic!\n')
    ClinicParserTest.assertEqual('stat($module, /, path)\n--\n\nThis/used to break Clinic!', function.docstring)

ClinicParserTest = test_clinic.ClinicParserTest()
test_parser_regression_special_character_in_parameter_column_of_docstring_first_line()
