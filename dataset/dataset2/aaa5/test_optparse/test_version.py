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

def test_version():
    TestVersion.parser = test_optparse.InterceptingOptionParser(usage=SUPPRESS_USAGE, version='%prog 0.1')
    save_argv = sys.argv[:]
    try:
        sys.argv[0] = os.path.join(os.curdir, 'foo', 'bar')
        TestVersion.assertOutput(['--version'], 'bar 0.1\n')
    finally:
        sys.argv[:] = save_argv

TestVersion = test_optparse.TestVersion()
test_version()
