from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_left_group():
    function = ClinicParserTest.parse_function('\nmodule curses\ncurses.addch\n   [\n   y: int\n     Y-coordinate.\n   x: int\n     X-coordinate.\n   ]\n   ch: char\n     Character to add.\n   [\n   attr: long\n     Attributes for the character.\n   ]\n   /\n')
    for (name, group) in (('y', -1), ('x', -1), ('ch', 0), ('attr', 1)):
        p = function.parameters[name]
        ClinicParserTest.assertEqual(p.group, group)
        ClinicParserTest.assertEqual(p.kind, inspect.Parameter.POSITIONAL_ONLY)
    ClinicParserTest.assertEqual(function.docstring.strip(), '\naddch([y, x,] ch, [attr])\n\n\n  y\n    Y-coordinate.\n  x\n    X-coordinate.\n  ch\n    Character to add.\n  attr\n    Attributes for the character.\n            '.strip())

ClinicParserTest = test_clinic.ClinicParserTest()
test_left_group()
