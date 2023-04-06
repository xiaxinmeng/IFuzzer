from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_scaffolding():
    ClinicParserTest.assertEqual(repr(clinic.unspecified), '<Unspecified>')
    ClinicParserTest.assertEqual(repr(clinic.NULL), '<Null>')
    with support.captured_stdout() as stdout:
        with ClinicParserTest.assertRaises(SystemExit):
            clinic.fail('The igloos are melting!', filename='clown.txt', line_number=69)
    ClinicParserTest.assertEqual(stdout.getvalue(), 'Error in file "clown.txt" on line 69:\nThe igloos are melting!\n')

ClinicParserTest = test_clinic.ClinicParserTest()
test_scaffolding()
