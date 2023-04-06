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

def test_no_single_dash():
    TestOptionChecks.assertOptionError("invalid long option string '-debug': must start with --, followed by non-dash", ['-debug'])
    TestOptionChecks.assertOptionError("option -d: invalid long option string '-debug': must start with --, followed by non-dash", ['-d', '-debug'])
    TestOptionChecks.assertOptionError("invalid long option string '-debug': must start with --, followed by non-dash", ['-debug', '--debug'])

TestOptionChecks = test_optparse.TestOptionChecks()
test_no_single_dash()
