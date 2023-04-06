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

def test_float_default():
    TestExpandDefaults.parser.add_option('-p', '--prob', help='blow up with probability PROB [default: %default]')
    TestExpandDefaults.parser.set_defaults(prob=0.43)
    expected_help = TestExpandDefaults.help_prefix + '  -p PROB, --prob=PROB  blow up with probability PROB [default: 0.43]\n'
    TestExpandDefaults.assertHelp(TestExpandDefaults.parser, expected_help)

TestExpandDefaults = test_optparse.TestExpandDefaults()
TestExpandDefaults.setUp()
test_float_default()
