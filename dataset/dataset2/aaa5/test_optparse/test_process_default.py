import sys
import os
import re
import copy
import unittest
from io import StringIO
from test import support
from test.support import os_helper
import optparse
from optparse import make_option, Option, TitledHelpFormatter, OptionParser, OptionGroup, SUPPRESS_USAGE, OptionError, OptionConflictError, BadOptionError, OptionValueError, Values
from optparse import _match_abbrev
from optparse import _parse_num
import test_optparse

def test_process_default():
    TestDefaultValues.parser.option_class = test_optparse.DurationOption
    TestDefaultValues.parser.add_option('-d', type='duration', default=300)
    TestDefaultValues.parser.add_option('-e', type='duration', default='6m')
    TestDefaultValues.parser.set_defaults(n='42')
    TestDefaultValues.expected.update({'d': 300, 'e': 360, 'n': 42})
    TestDefaultValues.assertEqual(TestDefaultValues.parser.get_default_values(), TestDefaultValues.expected)
    TestDefaultValues.parser.set_process_default_values(False)
    TestDefaultValues.expected.update({'d': 300, 'e': '6m', 'n': '42'})
    TestDefaultValues.assertEqual(TestDefaultValues.parser.get_default_values(), TestDefaultValues.expected)

TestDefaultValues = test_optparse.TestDefaultValues()
TestDefaultValues.setUp()
test_process_default()
