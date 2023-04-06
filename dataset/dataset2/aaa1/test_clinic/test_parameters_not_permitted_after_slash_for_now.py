from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_parameters_not_permitted_after_slash_for_now():
    ClinicParserTest.parse_function_should_fail('\nmodule foo\nfoo.bar\n    /\n    x: int\n')

ClinicParserTest = test_clinic.ClinicParserTest()
test_parameters_not_permitted_after_slash_for_now()
