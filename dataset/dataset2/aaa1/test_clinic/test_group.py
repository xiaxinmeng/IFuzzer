from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_group():
    function = ClinicParserTest.parse_function('module window\nwindow.border\n [\n ls : int\n ]\n /\n')
    p = function.parameters['ls']
    ClinicParserTest.assertEqual(1, p.group)

ClinicParserTest = test_clinic.ClinicParserTest()
test_group()
