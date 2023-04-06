from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_param_default():
    function = ClinicParserTest.parse_function('module os\nos.access\n    follow_symlinks: bool = True')
    p = function.parameters['follow_symlinks']
    ClinicParserTest.assertEqual(True, p.default)

ClinicParserTest = test_clinic.ClinicParserTest()
test_param_default()
