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

def test_default_progname():
    save_argv = sys.argv[:]
    try:
        sys.argv[0] = os.path.join('foo', 'bar', 'baz.py')
        parser = OptionParser('%prog ...', version='%prog 1.2')
        expected_usage = 'Usage: baz.py ...\n'
        TestProgName.assertUsage(parser, expected_usage)
        TestProgName.assertVersion(parser, 'baz.py 1.2')
        TestProgName.assertHelp(parser, expected_usage + '\n' + "Options:\n  --version   show program's version number and exit\n  -h, --help  show this help message and exit\n")
    finally:
        sys.argv[:] = save_argv

TestProgName = test_optparse.TestProgName()
test_default_progname()
