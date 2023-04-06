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

def test_get_option():
    opt1 = TestOptionParser.parser.get_option('-v')
    TestOptionParser.assertIsInstance(opt1, Option)
    TestOptionParser.assertEqual(opt1._short_opts, ['-v', '-n'])
    TestOptionParser.assertEqual(opt1._long_opts, ['--verbose', '--noisy'])
    TestOptionParser.assertEqual(opt1.action, 'store_true')
    TestOptionParser.assertEqual(opt1.dest, 'verbose')

TestOptionParser = test_optparse.TestOptionParser()
TestOptionParser.setUp()
test_get_option()
