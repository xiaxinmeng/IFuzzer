from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_param():
    function = ClinicParserTest.parse_function('module os\nos.access\n   path: int')
    ClinicParserTest.assertEqual('access', function.name)
    ClinicParserTest.assertEqual(2, len(function.parameters))
    p = function.parameters['path']
    ClinicParserTest.assertEqual('path', p.name)
    ClinicParserTest.assertIsInstance(p.converter, clinic.int_converter)

ClinicParserTest = test_clinic.ClinicParserTest()
test_param()
