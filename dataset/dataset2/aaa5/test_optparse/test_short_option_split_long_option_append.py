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

def test_short_option_split_long_option_append():
    TestStandard.assertParseOK(['--foo=bar', '-b', '123', '--foo', 'baz'], {'a': None, 'boo': 123, 'foo': ['bar', 'baz']}, [])

TestStandard = test_optparse.TestStandard()
TestStandard.setUp()
test_short_option_split_long_option_append()
