from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_disallowed_grouping__group_after_parameter_on_left():
    ClinicParserTest.parse_function_should_fail('\nmodule foo\nfoo.group_after_parameter_on_left\n    [\n    group2 : int\n    [\n    group1 : int\n    ]\n    ]\n    param: int\n            ')

ClinicParserTest = test_clinic.ClinicParserTest()
test_disallowed_grouping__group_after_parameter_on_left()
