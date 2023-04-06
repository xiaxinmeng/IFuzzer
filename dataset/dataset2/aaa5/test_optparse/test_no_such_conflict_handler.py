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

def test_no_such_conflict_handler():
    TestConflict.assertRaises(TestConflict.parser.set_conflict_handler, ('foo',), None, ValueError, "invalid conflict_resolution value 'foo'")

TestConflict = test_optparse.TestConflict()
TestConflict.setUp()
test_no_such_conflict_handler()
