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

def test_no_type_for_action():
    TestOptionChecks.assertOptionError("option -b: must not supply a type for action 'count'", ['-b'], {'action': 'count', 'type': 'int'})

TestOptionChecks = test_optparse.TestOptionChecks()
test_no_type_for_action()
