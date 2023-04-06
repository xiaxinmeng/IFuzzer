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

@support.impl_detail('Relies on sys.getrefcount', cpython=True)
def test_refleak():
    big_thing = [42]
    refcount = sys.getrefcount(big_thing)
    parser = OptionParser()
    parser.add_option('-a', '--aaarggh')
    parser.big_thing = big_thing
    parser.destroy()
    del parser
    TestOptionParser.assertEqual(refcount, sys.getrefcount(big_thing))

TestOptionParser = test_optparse.TestOptionParser()
test_refleak()
