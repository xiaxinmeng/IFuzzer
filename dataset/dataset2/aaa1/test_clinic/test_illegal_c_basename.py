from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_illegal_c_basename():
    ClinicParserTest.parse_function_should_fail('\nmodule foo\nfoo.bar as 935\n    /\n')

ClinicParserTest = test_clinic.ClinicParserTest()
test_illegal_c_basename()
