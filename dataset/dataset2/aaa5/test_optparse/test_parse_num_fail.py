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

def test_parse_num_fail():
    TestParseNumber.assertRaises(_parse_num, ('', int), {}, ValueError, re.compile("invalid literal for int().*: '?'?"))
    TestParseNumber.assertRaises(_parse_num, ('0xOoops', int), {}, ValueError, re.compile("invalid literal for int().*: s?'?0xOoops'?"))

TestParseNumber = test_optparse.TestParseNumber()
test_parse_num_fail()
