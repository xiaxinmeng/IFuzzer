import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_context_tb():
    TestInteractiveConsole.infunc.side_effect = ['try: ham\nexcept: eggs\n', EOFError('Finished')]
    TestInteractiveConsole.console.interact()
    output = ''.join((''.join(call[1]) for call in TestInteractiveConsole.stderr.method_calls))
    expected = dedent('\n        Traceback (most recent call last):\n          File "<console>", line 1, in <module>\n        NameError: name \'ham\' is not defined\n\n        During handling of the above exception, another exception occurred:\n\n        Traceback (most recent call last):\n          File "<console>", line 2, in <module>\n        NameError: name \'eggs\' is not defined\n        ')
    TestInteractiveConsole.assertIn(expected, output)

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_context_tb()
