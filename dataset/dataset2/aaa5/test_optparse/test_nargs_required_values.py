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

def test_nargs_required_values():
    TestMultipleArgs.assertParseFail(['--point', '1.0', '3.5'], '--point option requires 3 arguments')

TestMultipleArgs = test_optparse.TestMultipleArgs()
TestMultipleArgs.setUp()
test_nargs_required_values()
