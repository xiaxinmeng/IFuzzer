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

def test_parse_num_ok():
    TestParseNumber.assertEqual(_parse_num('0', int), 0)
    TestParseNumber.assertEqual(_parse_num('0x10', int), 16)
    TestParseNumber.assertEqual(_parse_num('0XA', int), 10)
    TestParseNumber.assertEqual(_parse_num('010', int), 8)
    TestParseNumber.assertEqual(_parse_num('0b11', int), 3)
    TestParseNumber.assertEqual(_parse_num('0b', int), 0)

TestParseNumber = test_optparse.TestParseNumber()
test_parse_num_ok()
