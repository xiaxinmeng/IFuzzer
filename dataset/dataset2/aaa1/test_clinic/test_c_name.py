from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_c_name():
    function = ClinicParserTest.parse_function('module os\nos.stat as os_stat_fn')
    ClinicParserTest.assertEqual('os_stat_fn', function.c_basename)

ClinicParserTest = test_clinic.ClinicParserTest()
test_c_name()
