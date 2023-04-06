from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_init_with_no_parameters():
    function = ClinicParserTest.parse_function('\nmodule foo\nclass foo.Bar "unused" "notneeded"\nfoo.Bar.__init__\n\nDocstring\n\n', signatures_in_block=3, function_index=2)
    ClinicParserTest.assertEqual('Bar()\n--\n\nDocstring', function.docstring)
    ClinicParserTest.assertEqual(1, len(function.parameters))

ClinicParserTest = test_clinic.ClinicParserTest()
test_init_with_no_parameters()
