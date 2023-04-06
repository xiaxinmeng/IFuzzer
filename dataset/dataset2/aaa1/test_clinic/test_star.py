from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_star():
    function = ClinicParserTest.parse_function('module os\nos.access\n    *\n    follow_symlinks: bool = True')
    p = function.parameters['follow_symlinks']
    ClinicParserTest.assertEqual(inspect.Parameter.KEYWORD_ONLY, p.kind)
    ClinicParserTest.assertEqual(0, p.group)

ClinicParserTest = test_clinic.ClinicParserTest()
test_star()
