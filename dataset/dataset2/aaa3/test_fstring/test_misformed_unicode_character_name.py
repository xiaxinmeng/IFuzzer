import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_misformed_unicode_character_name():
    TestCase.assertAllRaise(SyntaxError, "\\(unicode error\\) 'unicodeescape' codec can't decode bytes in position .*: malformed \\\\N character escape", ["f'\\N'", "f'\\N{'", "f'\\N{GREEK CAPITAL LETTER DELTA'", "'\\N'", "'\\N{'", "'\\N{GREEK CAPITAL LETTER DELTA'"])

TestCase = test_fstring.TestCase()
test_misformed_unicode_character_name()
