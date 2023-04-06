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

def test_numeric_options():
    TestParseNumber.assertParseOK(['-n', '42', '-l', '0x20'], {'n': 42, 'l': 32}, [])
    TestParseNumber.assertParseOK(['-n', '0b0101', '-l010'], {'n': 5, 'l': 8}, [])
    TestParseNumber.assertParseFail(['-n008'], "option -n: invalid integer value: '008'")
    TestParseNumber.assertParseFail(['-l0b0123'], "option -l: invalid integer value: '0b0123'")
    TestParseNumber.assertParseFail(['-l', '0x12x'], "option -l: invalid integer value: '0x12x'")

TestParseNumber = test_optparse.TestParseNumber()
TestParseNumber.setUp()
test_numeric_options()
