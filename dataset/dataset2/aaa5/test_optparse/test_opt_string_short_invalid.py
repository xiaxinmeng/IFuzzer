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

def test_opt_string_short_invalid():
    TestOptionChecks.assertOptionError("invalid short option string '--': must be of the form -x, (x any non-dash char)", ['--'])

TestOptionChecks = test_optparse.TestOptionChecks()
test_opt_string_short_invalid()
