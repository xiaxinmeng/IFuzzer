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

def test_help_description_groups():
    TestHelp.parser.set_description('This is the program description for %prog.  %prog has an option group as well as single options.')
    group = OptionGroup(TestHelp.parser, 'Dangerous Options', 'Caution: use of these options is at your own risk.  It is believed that some of them bite.')
    group.add_option('-g', action='store_true', help='Group option.')
    TestHelp.parser.add_option_group(group)
    expect = 'Usage: bar.py [options]\n\nThis is the program description for bar.py.  bar.py has an option group as\nwell as single options.\n\nOptions:\n  -a APPLE           throw APPLEs at basket\n  -b NUM, --boo=NUM  shout "boo!" NUM times (in order to frighten away all the\n                     evil spirits that cause trouble and mayhem)\n  --foo=FOO          store FOO in the foo list for later fooing\n  -h, --help         show this help message and exit\n\n  Dangerous Options:\n    Caution: use of these options is at your own risk.  It is believed\n    that some of them bite.\n\n    -g               Group option.\n'
    TestHelp.assertHelpEquals(expect)
    TestHelp.parser.epilog = 'Please report bugs to /dev/null.'
    TestHelp.assertHelpEquals(expect + '\nPlease report bugs to /dev/null.\n')

TestHelp = test_optparse.TestHelp()
TestHelp.setUp()
test_help_description_groups()
