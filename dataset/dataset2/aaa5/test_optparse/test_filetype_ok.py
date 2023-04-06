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

def test_filetype_ok():
    os_helper.create_empty_file(os_helper.TESTFN)
    TestExtendAddTypes.assertParseOK(['--file', os_helper.TESTFN, '-afoo'], {'file': os_helper.TESTFN, 'a': 'foo'}, [])

TestExtendAddTypes = test_optparse.TestExtendAddTypes()
TestExtendAddTypes.setUp()
test_filetype_ok()
