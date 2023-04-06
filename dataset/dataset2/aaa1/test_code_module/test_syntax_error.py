import sys
import unittest
from textwrap import dedent
from contextlib import ExitStack
from unittest import mock
from test.support import import_helper
import test_code_module

def test_syntax_error():
    TestInteractiveConsole.infunc.side_effect = ['undefined', EOFError('Finished')]
    TestInteractiveConsole.console.interact()
    for call in TestInteractiveConsole.stderr.method_calls:
        if 'NameError' in ''.join(call[1]):
            break
    else:
        raise AssertionError('No syntax error from console')

TestInteractiveConsole = test_code_module.TestInteractiveConsole()
TestInteractiveConsole.setUp()
test_syntax_error()
