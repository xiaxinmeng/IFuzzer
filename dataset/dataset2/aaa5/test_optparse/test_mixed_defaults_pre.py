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

def test_mixed_defaults_pre():
    TestDefaultValues.parser.set_defaults(x='barf', y='blah')
    TestDefaultValues.parser.add_option('-x', default='frob')
    TestDefaultValues.parser.add_option('-y')
    TestDefaultValues.expected.update({'x': 'frob', 'y': 'blah'})
    TestDefaultValues.assertEqual(TestDefaultValues.parser.get_default_values(), TestDefaultValues.expected)
    TestDefaultValues.parser.remove_option('-y')
    TestDefaultValues.parser.add_option('-y', default=None)
    TestDefaultValues.expected.update({'y': None})
    TestDefaultValues.assertEqual(TestDefaultValues.parser.get_default_values(), TestDefaultValues.expected)

TestDefaultValues = test_optparse.TestDefaultValues()
TestDefaultValues.setUp()
test_mixed_defaults_pre()
