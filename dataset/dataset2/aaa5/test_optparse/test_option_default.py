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

def test_option_default():
    TestExpandDefaults.parser.add_option('-f', '--file', default='foo.txt', help=TestExpandDefaults.file_help)
    TestExpandDefaults.assertHelp(TestExpandDefaults.parser, TestExpandDefaults.expected_help_file)

TestExpandDefaults = test_optparse.TestExpandDefaults()
TestExpandDefaults.setUp()
test_option_default()
