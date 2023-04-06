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

def test_option_group_create_instance():
    group = OptionGroup(TestOptionGroup.parser, 'Spam')
    TestOptionGroup.parser.add_option_group(group)
    group.add_option('--spam', action='store_true', help='spam spam spam spam')
    TestOptionGroup.assertParseOK(['--spam'], {'spam': 1}, [])

TestOptionGroup = test_optparse.TestOptionGroup()
TestOptionGroup.setUp()
test_option_group_create_instance()
