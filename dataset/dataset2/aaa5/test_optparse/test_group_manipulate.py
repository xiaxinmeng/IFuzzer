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

def test_group_manipulate():
    group = TestOptionGroup.parser.add_option_group('Group 2', description='Some more options')
    group.set_title('Bacon')
    group.add_option('--bacon', type='int')
    TestOptionGroup.assertTrue(TestOptionGroup.parser.get_option_group('--bacon'), group)

TestOptionGroup = test_optparse.TestOptionGroup()
TestOptionGroup.setUp()
test_group_manipulate()
