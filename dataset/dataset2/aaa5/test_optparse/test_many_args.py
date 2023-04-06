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

def test_many_args():
    TestCallbackManyArgs.assertParseOK(['-a', 'foo', 'bar', '--apple', 'ding', 'dong', '-b', '1', '2', '3', '--bob', '-666', '42', '0'], {'apple': None, 'bob': None}, [])

TestCallbackManyArgs = test_optparse.TestCallbackManyArgs()
TestCallbackManyArgs.setUp()
test_many_args()
