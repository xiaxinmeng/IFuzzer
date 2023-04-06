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

def test_get_option_equals():
    opt1 = TestOptionParser.parser.get_option('-v')
    opt2 = TestOptionParser.parser.get_option('--verbose')
    opt3 = TestOptionParser.parser.get_option('-n')
    opt4 = TestOptionParser.parser.get_option('--noisy')
    TestOptionParser.assertTrue(opt1 is opt2 is opt3 is opt4)

TestOptionParser = test_optparse.TestOptionParser()
TestOptionParser.setUp()
test_get_option_equals()
