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

def test_shortopt_empty_longopt_append():
    TestStandard.assertParseOK(['-a', '', '--foo=blah', '--foo='], {'a': '', 'boo': None, 'foo': ['blah', '']}, [])

TestStandard = test_optparse.TestStandard()
TestStandard.setUp()
test_shortopt_empty_longopt_append()
