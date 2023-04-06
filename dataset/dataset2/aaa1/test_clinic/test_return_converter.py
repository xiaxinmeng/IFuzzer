from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_return_converter():
    function = ClinicParserTest.parse_function('module os\nos.stat -> int')
    ClinicParserTest.assertIsInstance(function.return_converter, clinic.int_return_converter)

ClinicParserTest = test_clinic.ClinicParserTest()
test_return_converter()
