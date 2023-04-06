from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_parameters_required_after_star_without_initial_parameters_with_docstring():
    ClinicParserTest.parse_function_should_fail('\nmodule foo\nfoo.bar\n    *\nDocstring here.\n')

ClinicParserTest = test_clinic.ClinicParserTest()
test_parameters_required_after_star_without_initial_parameters_with_docstring()
