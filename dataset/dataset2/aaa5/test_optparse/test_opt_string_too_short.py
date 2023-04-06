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

def test_opt_string_too_short():
    TestOptionChecks.assertOptionError("invalid option string 'b': must be at least two characters long", ['b'])

TestOptionChecks = test_optparse.TestOptionChecks()
test_opt_string_too_short()
