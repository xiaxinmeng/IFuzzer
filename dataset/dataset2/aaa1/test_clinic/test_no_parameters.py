from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_no_parameters():
    function = ClinicParserTest.parse_function('\nmodule foo\nfoo.bar\n\nDocstring\n\n')
    ClinicParserTest.assertEqual('bar($module, /)\n--\n\nDocstring', function.docstring)
    ClinicParserTest.assertEqual(1, len(function.parameters))

ClinicParserTest = test_clinic.ClinicParserTest()
test_no_parameters()
