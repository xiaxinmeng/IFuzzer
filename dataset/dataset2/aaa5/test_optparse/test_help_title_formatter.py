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

def test_help_title_formatter():
    with os_helper.EnvironmentVarGuard() as env:
        env['COLUMNS'] = '80'
        TestHelp.parser.formatter = TitledHelpFormatter()
        TestHelp.assertHelpEquals(test_optparse._expected_help_title_formatter)

TestHelp = test_optparse.TestHelp()
TestHelp.setUp()
test_help_title_formatter()
