import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_cause_tb():
    TestInteractiveConsole.infunc.side_effect = ["raise ValueError('') from AttributeError", EOFError('Finished')]
    TestInteractiveConsole.console.interact()
    output = ''.join((''.join(call[1]) for call in TestInteractiveConsole.stderr.method_calls))
    expected = dedent('\n        AttributeError\n\n        The above exception was the direct cause of the following exception:\n\n        Traceback (most recent call last):\n          File "<console>", line 1, in <module>\n        ValueError\n        ')
    TestInteractiveConsole.assertIn(expected, output)

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_cause_tb()
