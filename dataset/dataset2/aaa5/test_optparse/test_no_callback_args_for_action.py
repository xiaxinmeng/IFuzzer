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

def test_no_callback_args_for_action():
    TestOptionChecks.assertOptionError('option -b: callback_args supplied for non-callback option', ['-b'], {'action': 'store', 'callback_args': 'foo'})

TestOptionChecks = test_optparse.TestOptionChecks()
TestOptionChecks.setUp()
test_no_callback_args_for_action()
