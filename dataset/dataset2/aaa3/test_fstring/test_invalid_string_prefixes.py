import ast
import os
import re
import types
import decimal
import unittest
from test.support.os_helper import temp_cwd
from test.support.script_helper import assert_python_failure
import test_fstring

def test_invalid_string_prefixes():
    single_quote_cases = ["fu''", "uf''", "Fu''", "fU''", "Uf''", "uF''", "ufr''", "urf''", "fur''", "fru''", "rfu''", "ruf''", "FUR''", "Fur''", "fb''", "fB''", "Fb''", "FB''", "bf''", "bF''", "Bf''", "BF''"]
    double_quote_cases = [case.replace("'", '"') for case in single_quote_cases]
    TestCase.assertAllRaise(SyntaxError, 'unexpected EOF while parsing', single_quote_cases + double_quote_cases)

TestCase = test_fstring.TestCase()
test_invalid_string_prefixes()
