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

def test_match_abbrev_error():
    s = '--f'
    wordmap = {'--foz': None, '--foo': None, '--fie': None}
    TestMatchAbbrev.assertRaises(_match_abbrev, (s, wordmap), None, BadOptionError, 'ambiguous option: --f (--fie, --foo, --foz?)')

TestMatchAbbrev = test_optparse.TestMatchAbbrev()
test_match_abbrev_error()
