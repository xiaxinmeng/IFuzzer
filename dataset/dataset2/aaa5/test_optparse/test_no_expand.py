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

def test_no_expand():
    TestExpandDefaults.parser.add_option('-f', '--file', default='foo.txt', help='read from %default file')
    TestExpandDefaults.parser.formatter.default_tag = None
    expected_help = TestExpandDefaults.help_prefix + '  -f FILE, --file=FILE  read from %default file\n'
    TestExpandDefaults.assertHelp(TestExpandDefaults.parser, expected_help)

TestExpandDefaults = test_optparse.TestExpandDefaults()
TestExpandDefaults.setUp()
test_no_expand()
