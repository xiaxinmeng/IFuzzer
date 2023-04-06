from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_disallowed_grouping__empty_group_on_left():
    ClinicParserTest.parse_function_should_fail('\nmodule foo\nfoo.empty_group\n    [\n    [\n    ]\n    group2 : int\n    ]\n    param: int\n            ')

ClinicParserTest = test_clinic.ClinicParserTest()
test_disallowed_grouping__empty_group_on_left()
