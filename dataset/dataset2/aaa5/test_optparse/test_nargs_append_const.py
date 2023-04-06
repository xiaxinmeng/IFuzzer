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

def test_nargs_append_const():
    TestMultipleArgsAppend.assertParseOK(['--zero', '--foo', '3', '4', '-z'], {'point': None, 'foo': [(0, 0), (3, 4), (0, 0)]}, [])

TestMultipleArgsAppend = test_optparse.TestMultipleArgsAppend()
TestMultipleArgsAppend.setUp()
test_nargs_append_const()
