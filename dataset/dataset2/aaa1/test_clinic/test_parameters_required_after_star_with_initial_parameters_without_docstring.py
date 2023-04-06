from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_parameters_required_after_star_with_initial_parameters_without_docstring():
    ClinicParserTest.parse_function_should_fail('\nmodule foo\nfoo.bar\n    this: int\n    *\n')

ClinicParserTest = test_clinic.ClinicParserTest()
test_parameters_required_after_star_with_initial_parameters_without_docstring()
