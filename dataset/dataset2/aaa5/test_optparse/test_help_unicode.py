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

def test_help_unicode():
    TestHelp.parser = test_optparse.InterceptingOptionParser(usage=SUPPRESS_USAGE)
    TestHelp.parser.add_option('-a', action='store_true', help='olé!')
    expect = 'Options:\n  -h, --help  show this help message and exit\n  -a          olé!\n'
    TestHelp.assertHelpEquals(expect)

TestHelp = test_optparse.TestHelp()
TestHelp.setUp()
test_help_unicode()
