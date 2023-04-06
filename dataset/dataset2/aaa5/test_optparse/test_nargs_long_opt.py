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

def test_nargs_long_opt():
    TestMultipleArgs.assertParseOK(['--point', '-1', '2.5', '-0', 'xyz'], {'point': (-1.0, 2.5, -0.0)}, ['xyz'])

TestMultipleArgs = test_optparse.TestMultipleArgs()
TestMultipleArgs.setUp()
test_nargs_long_opt()
