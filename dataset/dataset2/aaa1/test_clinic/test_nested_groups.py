from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_nested_groups():
    function = ClinicParserTest.parse_function('\nmodule curses\ncurses.imaginary\n   [\n   [\n   y1: int\n     Y-coordinate.\n   y2: int\n     Y-coordinate.\n   ]\n   x1: int\n     X-coordinate.\n   x2: int\n     X-coordinate.\n   ]\n   ch: char\n     Character to add.\n   [\n   attr1: long\n     Attributes for the character.\n   attr2: long\n     Attributes for the character.\n   attr3: long\n     Attributes for the character.\n   [\n   attr4: long\n     Attributes for the character.\n   attr5: long\n     Attributes for the character.\n   attr6: long\n     Attributes for the character.\n   ]\n   ]\n   /\n')
    for (name, group) in (('y1', -2), ('y2', -2), ('x1', -1), ('x2', -1), ('ch', 0), ('attr1', 1), ('attr2', 1), ('attr3', 1), ('attr4', 2), ('attr5', 2), ('attr6', 2)):
        p = function.parameters[name]
        ClinicParserTest.assertEqual(p.group, group)
        ClinicParserTest.assertEqual(p.kind, inspect.Parameter.POSITIONAL_ONLY)
    ClinicParserTest.assertEqual(function.docstring.strip(), '\nimaginary([[y1, y2,] x1, x2,] ch, [attr1, attr2, attr3, [attr4, attr5,\n          attr6]])\n\n\n  y1\n    Y-coordinate.\n  y2\n    Y-coordinate.\n  x1\n    X-coordinate.\n  x2\n    X-coordinate.\n  ch\n    Character to add.\n  attr1\n    Attributes for the character.\n  attr2\n    Attributes for the character.\n  attr3\n    Attributes for the character.\n  attr4\n    Attributes for the character.\n  attr5\n    Attributes for the character.\n  attr6\n    Attributes for the character.\n                '.strip())

ClinicParserTest = test_clinic.ClinicParserTest()
test_nested_groups()
