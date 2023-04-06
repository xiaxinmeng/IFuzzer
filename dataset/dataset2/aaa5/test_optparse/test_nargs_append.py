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

def test_nargs_append():
    TestMultipleArgsAppend.assertParseOK(['-f', '4', '-3', 'blah', '--foo', '1', '666'], {'point': None, 'foo': [(4, -3), (1, 666)]}, ['blah'])

TestMultipleArgsAppend = test_optparse.TestMultipleArgsAppend()
TestMultipleArgsAppend.setUp()
test_nargs_append()
