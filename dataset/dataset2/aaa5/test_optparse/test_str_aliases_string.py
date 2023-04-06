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

def test_str_aliases_string():
    TestTypeAliases.parser.add_option('-s', type='str')
    TestTypeAliases.assertEqual(TestTypeAliases.parser.get_option('-s').type, 'string')

TestTypeAliases = test_optparse.TestTypeAliases()
TestTypeAliases.setUp()
test_str_aliases_string()
